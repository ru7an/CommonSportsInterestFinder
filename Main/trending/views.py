from itertools import chain

from django.shortcuts import render
from home.models import registration
from discover.models import followers

from home.models import userpost,Like,comment

from complete.models import userdetails
from discover.models import interest


def trending(request):
    try:
        if request.session['email']:
            email = request.session['email']
            user = registration.objects.filter(email=email)
            usr_id = registration.objects.get(email=email)
            usrs_id = usr_id.id
            other = None
            my_id = None
            counts = 0
            count_following =0
            pu = registration.objects.all()
            qs = None

            try:
                em = followers.objects.get(user_id=usrs_id)
                other = [user_id for user_id in em.following.all()]
                count_following= len(other)
                my_id = [user_id for user_id in em.follow_me.all()]
                counts = len(my_id)



            except:

                pass


            try:
                profile1 = registration.objects.get(email=email)
                profile = followers.objects.get(user_id=profile1.pk)
                users1 = [i for i in profile.following.all()]
                posts =[]
                for u in users1:
                    p = registration.objects.get(id=u.id)
                    try:
                        p_post = userpost.objects.filter(author_id=p.id)
                        posts.append(p_post)
                    except:
                        pass

                my_post = userpost.objects.filter(author_id=profile1.id)
                posts.append(my_post)
                if len(posts) > 0:
                    qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
            except:
                pass
            interest_list = interest.objects.all()
            user_data = userdetails.objects.all()
            mydetials = 0
            try:
                mydetials = userdetails.objects.get(owner_id=usrs_id)
            except:
                pass

            my_post = userpost.objects.all()
            trendingpost = []
            for ids in my_post:
                if ids.liked.all().count() > 1:
                    nu = ids.id
                    dat = userpost.objects.filter(id=nu)
                    trendingpost.append(dat)

            trend = sorted(chain(*trendingpost), reverse=True, key=lambda obj: obj.created)

            like_unlike = None
            try:
                like_unlike = Like.objects.all()


            except:
                pass

            comments = None
            try:
                comments = comment.objects.all()
            except:
                pass

            dict1 = {
                'email': email,
                'user': user,
                'others': other,
                'followers': my_id,
                'count':counts,
                'count_following':count_following,
                'interest':interest_list,
                'posts':qs,
                'pu':pu,
                'mydetials':mydetials,
                'userdata':user_data,
                'trend':trend,
                'like_unlike':like_unlike,
                'comments':comments}


            return render(request, 'trending.html', dict1)
        else:
            return render(request, 'index.html')


    except:
        return render(request, 'index.html')