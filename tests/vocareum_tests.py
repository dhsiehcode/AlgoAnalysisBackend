import base64
import gzip

import shutil

from flaskr import vocareum
import zipfile
import io

auth_token = "b7ced88c162ce28340e00851f5a216f4259e69c6"

course_id = '101632' # id for automatic runtime analysis



## passed
def test_get_courses():

    print(vocareum.get_courses(auth_token))

## passed
def test_get_students():

    print(vocareum.get_students(auth_token, course_id))

def test_get_submissions():

    vocareum.get_latest_submission(auth_token=auth_token, courseId= course_id, assignmentId= "2336373",  partId= "2336418", userId= "1584772" )


#test_get_submissions()


content = "UEsDBAoAAAAAALpkblcAAAAAAAAAAAAAAAAiABwAc3ViX3UxNTg0NzcyX2EyMzM2MzczX3AyMzM2NDE4X3MwL1VUCQADn9pTZZ\/aU2V1eAsAAQQwAAAABDAAAABQSwMECgAAAAAAumRuVwAAAAAAAAAAAAAAACcAHABzdWJfdTE1ODQ3NzJfYTIzMzYzNzNfcDIzMzY0MThfczAvdGVzdC9VVAkAA5\/aU2Wf2lNldXgLAAEEMAAAAAQwAAAAUEsDBBQAAAAIALZkblcGDtL8gQYAAD4bAAA1ABwAc3ViX3UxNTg0NzcyX2EyMzM2MzczX3AyMzM2NDE4X3MwL3Rlc3QvUGFydDFUZXN0LmphdmFVVAkAA5faU2WX2lNldXgLAAEEMAAAAAQwAAAAzVhtc9M4EP6eXyE6c+A0wXnhehxN25lSykxnWiglfLjhmBthq4nAthxbLi0H\/\/12Jb\/Ir6mBD+cpCZFW2t1nn12tPNndHZBdcvKWzPdm++QFlZS8lVHiyCRiMaGBS469lYi4XPsxSl5G4hNzJJnvk0saydmSxRLGJ4PBgPuhiCT5RG+onUju2buL+tgVbCn8BYiHyUePO8TxaBwXe5F\/BwSedDKWVMLXcRTRu3Mey4OTJJbCZ9HryGXREXHSn\/GiYRUPJPxz2W3bpOQ+I4dk2joP9rxKfC3SIHMjuEt8ygMLIOPB6v0HQqNVPEx9wCc3EDYJ2JdWT6zhIl+Dqh0aUofLO1g2m06LuRWT2cLYyoSMta1IeTDWwwZXgKeMxI6ImOE\/PpOJitMsH0hhGo2K5Xrd6FDNzf6ZW+TJfAwUGys7hvXd5r12ezougLVj\/pVZw2LnfNnbu1gy3xaJtEMIj\/QCa+fvYLfx2TFtyry+oHJt+\/TWmtrTsR41xfg1sVJRiNKf9tQMfLsBSyGpl+q4FpGiPoHcm+\/Z0wl+7Bhx+E6YF7Of2nfatO1Af2pSR\/yGSpaxOg19hrXKonFGynE3w0wEOuB\/zlY8ICrwO2SU59mI7OTBKJIBEhhiwYuhkt43CUsYcTYpt+tzmCWdxC6Y6KyZ85mIkEUAhAhiIgLC\/BCy0NlscevkDeGxFrZtu+QAsMTZpCxFptRoktN7au8tJhP47A6\/UnsRr6xrCpNjsoN7l6Nb1c7jUzTNGm7RPbOnPXWnO3erh6p1AWmk3A8Sz9tqRV8EtIJuI1zm9TFi3hsKraDFiMmEBzGDjIyBnkX16qTVsevCqVJZUaWX2rU4EzALoTpuxgSJTyZkPuwiI4qnP7fiUQ1KP1Ki6gc9qPikhn9vIjawT\/kLA9a0XT8kAej\/vXf8m0hYMcXkoDIlYr64YWANefiQ9I6MtnSvJ1IFTw12XnPPI0lI5JqRDdbNTma+BGmkZroADL8vK5GUj0vOVSmCRfgy4thz3qUVHNbV49Vk19mrk9dXpydLcnl19vrqbPkXefPu9N2paVoBIDJt2lUxfiRN9n5BmmCWKACtIuuRs+osHCqDHs9+gjB\/9LRRG1MhjGYuoUAb+C80wciHel37KITHaEBC7PKhg4sSVjj7Zc3hLLYeKNNbC0PpTCeeQ6q5s+gQ36C4kXllWUQbNnxwCHJVtQoKbbUCYlGbbWIgKDGa\/kBIwjYJ9aoMzHE+vQ2PHQlG2FLoWwT2shvzZ8PSjxGjn8vD32uO3T+V2py5Zzrh05hSZbu+VxLdPAvKBGxEHRfhTCu55yoBn\/1QNSRJALdT3cCZ7t2v1W7qZPfVQHZpyPaLGFysAz28MJvwpk5c3S9zg81MYu6YaHoQn8m1cE1QMqCYW4a1wRe9GM1NtzV9r2HXvcE1hWTON2i+WxQepbxPnWC3Ye4QdbZeI2AxcyRzNcaweEvEQBPkoJbG7beaWD2\/Oi894+Ybib4zBYlfig1eowSQrXz3SAuhnjmoLsKnXNVUUWs4G8qpZ5wj1bqnhpcCXcoO55qIc4Z7VkumstG8nXfdJQ0wU2V9kCSlmoyJpm+jCjv4OjDPPBgYjaqoqdPUdoQf0ogthZW3fxxq4FH9KoaPkqGua\/E6KPjoFN5e5PJ9nO18K73WMd\/\/oIEl8njsWp5znyOBnj1dwEEMQ1ICWI\/oo5JkxFfrXHQ2n5dkv5ZlJY3ABJ2A5yxYyTWseVr4qN\/akUh\/6au2HrPMrqApRJknjfFJU37FArxzMzf9fZhqAvpKaB4zl8emTyMyG9Zig4\/t4bxVd6lF3BGex\/JS9DzhHlBvfx9czEpSPkbDkAXuiXDZpQDTWuZb9BQHuoEYPnXvqyNYXrF2\/Twqe\/8bEHKneAWOcgkQ6rPh5Y5VAWmsXueOoTOu5CwOm\/UKn6J2YoIqHWZU0kztrGlZdSwVd\/2uShdjFQvyW+1NZVcxyM74hs6t44zh1RMGuYF2zMkuToIhi3ppKAnMW16vvf8APY0f6h4a8kkNqkJu4lUy+1wrr3RvJZGrVH8qU+pclO0HqTropZTG2FIXZDTlPQp8yG15wTx+w6K7JUQZhI4OtRBvk6hWINPkln4ZFdZfyea2Hh02GPvtm2Fs2xsnU3f5YtT4wiHtHSvAVq6tOrRd+CmJXwxgFtAWBJXKZgi1vZ0YaoM7Qcz0\/woUU4EiOHjRzpXk2Qt\/g\/8AUEsDBBQAAAAIALZkbld0I12PhQkAAG0tAAA1ABwAc3ViX3UxNTg0NzcyX2EyMzM2MzczX3AyMzM2NDE4X3MwL3Rlc3QvUGFydDNUZXN0LmphdmFVVAkAA5faU2WX2lNldXgLAAEEMAAAAAQwAAAA1Vpbc9u2En73r4A9c1LKkmVJrpupb2cS12dGM4nj2s7DGR8\/MCRkIeVFIUHHauv\/fnYBkARAkJJjP7ic1oqIXWAv3y52Ae1ub2+QbXJ6RSb74wPym899csWzIuBFRnPiJyF5F92lGePzOEfKiyz9SgNOJgfkws\/43jXN+QYM7G5ssHiRZpx89e\/9IUuH74vZjGY0vKR+SLNDe\/g\/LKItQ9NPZw8BXXCWJuZYToMCRFkOz9OrIphXkrWQF5xFw+3DjY1F8SViAQkiP89rsclfGwQeNZhzn8PHuyzzlx9Yzo9Oi5ynMc0+ZSDjCQnU1\/zQwcUSDv+H9KFtkLOYkmMyah0Hec6LWCPJ2L3P6UqxIngHGiKLY+r7lIUk9lnigVNZcndzS\/zsLu8RPs\/S7zlps6MyDT6XgIE0Jnc0AeES+l298K6WOafxEByS0YRfg34fWQTSeL3eYcVcGU3x1mqceBoZWiDwF34AvgVKWGuY0Ac+Tbi3P+6RPhmPRjo1GLq2FD6mefG5o7y0VO6Vc2tLvqec08ww5u8FLSgJvilZ2yhcs4UpmB2cFaSZkGM4Uj7BZ3eXJTkFUOYwUW2SalxZMi34ELye8Cjxtt6FIbhLclR6DIfDLctqicCMbrDJCA22t1\/TIURW2R\/l0+z1bYAzA0WtBZsRD2ca5uxP6vXI5jGYSn3paXhp0+gKKHMwFElSDpDkwZz4MzCwWjzf1FXDpzTmznio+fVRM2swp8EfZJHm00R4phr6kqYR9ROywHgHOZHuoiID9XTdQS+ks3WQy\/ePyT4sv7sLf2sZCI1yatELRT\/md97Mh8EB2arlMhXV9Xzc6FBHsYU0+ug\/dKLlNxpRjniJ\/YcKLjZaLP8dA0zX8Buy9FzmNwIDFx6DpcUCGY3Te+qNNLYG8YQI+EjdPEtMOdmxpHvzRnwOIaA1Fwr5d8atTpsIp719vtOkhFtOE3SGxI8HhFxSxIOGjmIR4n7gV7YkPCVzdjfHnYwl9\/ARQyLuxMnn9eZw5BlmZRld7V0ywZRjvSI7ZNwGgMCCCtNVBRNKXb0AnX7uxzDjAF\/DN4EW\/IeYCHDP7mm2xN0HVoUVLSQFCBMNZyvw8uuT8aK8AmaMfwglz0mccu2186YOJml3DQidsLlEakwvfmtyeSY8XIBogY7KHIpQg4jT9SJ\/BC3ZA8c2WbkpTBBjqxAyHj8ZIlJS20uC7Oxh8S7goARPZX0mgD7RvlpcLu9MZ1DNaVWCxMhA7now5HN9T2E5ySlHwIL+WN4LAn0CJMmoH0VLIkUPySyDChBpvuEcm68c5zXM1c6fMSxvl2aNgOJuNsdF7TNaS+Dp+emny7PTa3JxOf10Ob3+L\/n989nnszY5RyvDMaeQzPyoduV6Udlgs4JTVUHQ1dH65SzNiIeZ\/auom+HjyIjg8UjW3TDS79vW6Ah3S\/muwBbj64Rz6a5AYGpiSyN0dEddaRvbJ5pZBINjVI9PTBdJEUXk32QLP7fIAbGD1knTEcr4fIE4+8N8\/Wh864ZwaZf1YYzPM6CMjxPOpuRmTugsrlVW3dOz6qvLKLU3ypxKXV3Hi3Qbe9IgvzS2mSfWrVlrdtgy2rp\/TpJUpZbSZ3Wdu05qBPqbWxKy2aw8oRBv\/trZG5AdKAh2xgMC\/8G\/9h67c+ezM+X3OYsoTAtzNfqyFj3tZPq0Bc1Mg+qgHYBdmONGn0S8GUY0uePz3u1hgxEMp5fiZc6HXA4ytlXrfbFQM8vbkx05J7uI\/ICGcqpewwr2HNjGWxtP1WVYs5f9hjWFZTzJO03wLMVjXdSPL5sffhb5YTJ6fmcrVcj\/IcXca8pERD\/Pi4G8MxlNBbE4ncGZ21MRnmrilmgcdTYP5qoDxNI3O5JX76Ffi\/tqm7We1a0bFZvtYWGvK6ZdiX\/hje4zudcEOnmEQYqEs4jQeMGXnagzjgSBRfGs0xqonWhTAIjlZ8jXhI3Zli+gVNbT\/shS0KKGqlrW\/eWRTnMbEDMCbpF2rYq\/aSBn1a\/V9biEUcXj2+6KvbtpcNXzruSMj\/P0s3zazlHFjA1TrRvp+LxEtOPTHnk\/1AfIQ\/aJccpuXT6oFSFBAtU6sfe\/5DrlUPxJRiza8OqP7B3ganigD3ohb\/dG+rSZR9XMdj4p1RF\/rNs9cU1nlhR45jooi6tG+aSrv\/potaQMhrmrFHMuYO9B16mQK1ADSimXHlVg6rcwNBwQGVYkpnyehroGJTpouPLUXDJD7bilptUt3WiTuieY+ZDnqglWaaRyhlKCPiwqhXwzQbkAA8w04DQ8gGX7yKxJ7bz+C3jhR5Iap18pol0odFxvDsqLw6fcAosb2hRyq3nLqrYKOXIkbiPfvFGlzFGjUuneQhC5NYcoyFVZo\/NAcpO6VlCsRQymyGDnUxENfhg2GITU\/b5dr3RY2bhU1i+tUTPDVhGd8Q8sZmivX98eYtEYCZeQn\/yfDMqM3c0r0vFkYtD+adJyPwMRJOw+iG4MeN7WCqi7+kx+GNf1enVY9a9M9q\/Yc5aawLdmF6uADi0hdNMAY\/X9WK0EHuG5V6k80HXqk3GzPcNnGOG411SphTxIo4hWAfi+YBGA5uAAVCwDsXrnLxY0CU\/TkF6kIFrLeMs69favWQyfpvb2G0wqGLHPt8r+qzFCpRSzzGEGbyr+SsQZI55lpIH4rQaerFjRiK\/1YMSnTgcYv2IN3Sv1zoof7rRY5gQjl8nfj3iq5QJfkH81klVXyi13Nrtp6ci6rTu2+ElO5i+reli8FZutZiFXyAo2dSrjDFvcVwXRDbvFwhCPpV01oU7XuCkDPuZiwse1dWl9VphCWVnXlMLcrlpSWbjaY7cE3qCkF9tfi2At82SUF1nSVqCbtbOrUlX8dUe0ctNVlZHV4egmczlPq9lbfbeAeI8XfkavU\/2UqkdO3EeE1U4Htls47CN1W12tV\/MszChQXXyOwlW3hQHeF6pfgUVLsEl9UdgVOuW1q1UDDLp+mPVaYghrHB2W8shwSL9BzZYbd1jN9NrAlxN+GnzXyUDG4cTK0o\/1rMIO9yjMhxOyjYN9\/Wa+KlEMgslhqyMgISzcfqhYDOE\/yMWtgDVILtX6isY85UL2I7XceRGLFXPIW+AjFOUGCW7bzqBPjiURa6Ow4aCL3HIwhAvq7Z9sKitZT44dwv79tyZseZPYtbaFH1fj6s6E1umWdG2X\/QTFCxuwdGiLBcWSbhNKeTttKAXuNGK5\/ktYURHUzsEfnFSLVDGM7f\/\/AVBLAwQUAAAACAC2ZG5XFt64cqIHAAAkIgAANQAcAHN1Yl91MTU4NDc3Ml9hMjMzNjM3M19wMjMzNjQxOF9zMC90ZXN0L1BhcnQyVGVzdC5qYXZhVVQJAAOX2lNll9pTZXV4CwABBDAAAAAEMAAAAO1ZbW\/bNhD+7l\/BGmgrx65kO8m6xUmHNOvQAH0Jmnzr+oGRaFut3irSSdo1\/313FCWRlGTHXTYMQ4U2kkXe8V6fI0\/ezk6P7JCTczLdnxyQ36ig5FzkK1+scsYJTQJyHC3SPBTLmOPMszz9yHxBpgfkjOZiesG4gPderxfGWZoL8pFeUTdM3eer+ZzlLHjHaMDymT38exixjqHTty9ufJaJME3MMc78FUjyxX2Tnq\/8ZSVYx\/SVCCN3Z9brZavLKPSJH1HOa6nJnz0Clxrkggq4Hec5\/fIq5OLwZMVFGrP8bQ4yPiO++slnLVRhIuB\/wG66BkUYM3JExp3jIM+bVdw1pVOqCN6Bgi0kV2kYkJiGiQPuDJPF+w+E5gs+IGKZp9ecdJlQWQWvSmUQK2HXnVI4g1lFg8r4NKM+uAnIJuNxPbZgoiTkTjlJo12r5RYyBClYghHup7kyejXkedLzk+qFMvxwWJMXdMMjOTbRGVtTjshrKpZuTG+csTseFW8H2mrhnDhqKphi6o4HmnXxOv\/CBYvddCXcDJwkosTp\/5GgiJzM05xkEKtkCjfOWdDXJFlDnAoaKQGRxZlkcUD6ZAgp7o7h1vfwQWd3S1jE2fcJN6eQyfcg3LhLtsKe6gbMrqhgZZQrVytPbRHb7fLt4PWcLcKEyDhBucrUBNnkcF\/38DsAyDSGyE5UfBYvHMUe4CpnibiA7H8dRhDGzqA7V4CJm7AbcZoIZ38ygAWN7DHi\/SXlSyIo6l6s2xjVE2xNZtSyAHpZQkzGAyN1\/CXzP5E0YzlFa3ICFmVxBsK\/vNhg2JcXJOTFZNd1dfdijkhFXB5+ZeBDSJVGnlQpOXHHM8+Dv+tDV678mi+cOYXBEekj75agKvRCpVEnViPeRszSyMOEMwhjDnNaGLTZ4zgIAJEtCtsuEByJrAi6S6bjIi7qea3YaEEyyldrIa09QuY2Vtl+QN7q5waPTO\/XIzmL0ytmGojMc8g0KWI18zJNI0YTCZBgBNi3ME2lNtO\/0zifdJje4Fa+RLhy0CmfZOLA7dDwzB46Zp88eiTJYXw4tG2G1B8th+omNhHUyGiSTYjyR2Eb5+P66VNUQLpTzc8mLsTyGxo3V0LXA\/8HR0Bmy6zZQ3pu1hhts3JlWVKsHgDykCQVsCER\/tK1i0UVIC9usmNfoKwiLbYtzmAEUmk\/LdLbhiaaRVElPabvR7lz4MW3Uwg8zRYsr9XQ3T4ijWFDaFtjz3uqZ5uRwahNZ6pCkm4o+Y0sLdxn5amWqDQIoOgycDOgUDqXz2XC3gUCu2ibaNiKYfV05fAnmKNYyYYS3waz3n0h3O79IlxRSyEjJbBQMgf8zovNRAV4sAsx4a41GhnN\/aXkIkFNMbGx7c44tisrzP4\/CGCgdAO9irgnmIk6UN0R4pAj3xLU1sOWnt2b0QojKVlFEfmV9PHeJwekgWGtk9Ygm1ymE5xu28IKdX7QBgGN2ASLmaFZPrUEtoEfELr7Bvp8R9X+V+uyiucfhflHYW5R6P9VmMtHz+N1VaB1LqJdti0qtApgg9xKTYXfCZVtrirMCIZ1v+MMW6RO4\/DqIJMRGcO\/QSelif1IYR0pa7zdUNd\/3rquW9hph1QB7t3JUcdFEwu+T5FpcSgeb61JM4i2V6Z67OrMvf9AIL4y3WFyqmMpipPciCULsUR4QEwEKD7LQwDG6uB9lwbaaQKGybFHjX0QuaitYtUAMRJv\/cnR7l2JlgZR0ckqen7enitLTx+3jroAOROrPCk4zdb0tmQHt\/KZftRlwajMuJiJZRroZinRhgWDTaYqiFHGlhYjBtAWDMw24CaNVHgpJdhNVilEfTHY0KcDYvAuCwprA7EORG1nDV+saFTMRvYbRbRPG83Wm\/95VHZotuk6yo5fukqE2Xy7XoLtiFOMHMq2D2xXioPMYeOQY+eACY0+sK4pEB0lHysB\/M9uthKOb284Ev8UZ9s7b1kV4azXIJAi683z2022NRpqegcU1TIMFbG5eBXGIRrrl6e484RXQoCOj+ljY2YeLpbV1Ml0asz9as4VNAcRimB7VaDNEXlaK6A6uuoYZTR1W49RYbHtDNFRShP41dxjqvAuW42B+n2kVnKBF3cqlUe6TkMyMVO5vNwIx52mSh3T\/TSKWJV2z1dhBBFzcAAqlulXvaNZxpLgJA3YWQqidYx3rFOXCs1ieDW1t98glGCe\/n2r7P9njFApFVrmMDM3lX\/bdkSWkUbyc+KIPJlY2Yiv9WTEq8YCzF+5hu6VtV9XFBiWmGAAWfG5oOq2TAbkYQOpDKD1POx2YJMHj1i4FOwVAeoucT9HnuEeJ24TApPM2AxUuGvWPNksh80Q+faNqOdd0zWq8MLgzEQa2AcRuT7o8JM2xq9DOEQQB8btdPYpbK\/GB813eweNcEjM74vldZkz+mnW5DBt5YAbvd27M9ntZDLdyETbCKnK9CDkhe1lU80+PSvjg+3Q6Ptth7n2tVt3qdr0vTv0PHSnakOeFzCA\/zhM4EgIEtIy1J6RXfwUJcOvLdzKfVap8Zpoe0imrV+rlEjWyfXWjDnMnt2ugnJTFBRUCh7QcN1GD1tl6JZjkyXr9gqMYbe39xdQSwMEFAAAAAgAtmRuV0tQSMwjBgAAkRgAADUAHABzdWJfdTE1ODQ3NzJfYTIzMzYzNzNfcDIzMzY0MThfczAvdGVzdC9QYXJ0NFRlc3QuamF2YVVUCQADl9pTZZfaU2V1eAsAAQQwAAAABDAAAADNWFtzEzcUfvevOMkDrLGzsRMM01zo0AAzzFBIm\/SJ8qCsZVt0vVq02kCA\/PeeI+2upbXWJoV2qokTRzo6l+\/cJIllLpWG9+yaxQVPSiX0TfxaXpTJ4mk6l\/jvYvn8U8JzLWR23BMOealFGj9Vit28EoUOrP3OsqlcHvd6+w8e9OABnF3AwWR8BM+YZnChVZnoUvECkAwaYQVRniv5nicaDo7gnCn98JIXGuf3e728vEpFAknKimK1Bl96gCNX4pppDoVmGoka3U7OykLLJVdv1JSrJ5BU\/xbHdpvluW2XyH4recmP9\/frhQLnQC84fKCFu\/BKDWIBnUWmQYslDy6azRc3hebLX+WUp7Ck3518ciUTXhSXhh2Odf2upZjCkoksQneIbP72HTA1L\/polJIfC+gKhApvGldSppxlMEvZHE4BvVrpTsNGACj75xQy\/rGai\/orKtI1YTlLMPaQyFLHGf+kX2Y6moz7MIDJaEVP+CCdM+NY6i80nq6ErxzyxNfAuHYzEflsM4VxR0XS9lVUW9g\/rlxBY851E0weRU2wv18bBzPk2tjT89DLyuU6cAcjA9xKvZlUEBG5MCDhnxPaiV8Gg77jUgdR17pbR+aMGBnM4kJ85lEfdk6t+TGaZGwneKJ+tdxmb4GJZaljDNxMp1m0+zJLpFKU9rQH2ExzhXpw0gNjE5iPwK6jmrHOBuCMpQX3lG6+f1yIlEMU7TQ8YlE8X+b6BvX\/+hV2apOa2T7cu2cYt\/U36bUO+Xg0amlFSOVwcgqHozaPLhzOLfTW5FrVtrUdPjImA0cIVpIffbPkM7nMU65JMlkEkvwYkkyrxsnbZD\/+dtksS3iaGquzbsnEOTGklXw4PYW9cUhKlyS73YoAQTW8iruQPBrhyHLHleLsr\/Wl2xA23wbHH\/mU6W1glETEw44IZgCh52dp8Yyn7IZPI6oVrSXrkvDam4yKrc37pm61bOvMSFednVB6hRD5M7uUmqVQoLe4qWXU\/uHwCHZRvVE8wt+7+5N45CIVxPwO3B9a7pMO7tYUQrgXasKmvTZZeoemaqJ8vUj1PTMUx+NTttZs5zzb2Gmp+CNNU7NWcqpSvSL3Di2Q4MYVseJLec0j4ZDbMwRkzHRhGzC19QmFzmtGITOEpImj85QlfGpDyZ3HqBTXXN3YFdcCRMYIwLjLyjRdL8y2hLPpNEoCtXiHNsf8Q4lB6SrVwtbiSxa+UHJpWhlt9HzvREDI706NvKPnA23oy0bP3250QWKrOn8dKtrb8PznINhTnVup\/xUU3NPe7ffmgn+m2ZgJNWkgDxK8SelzWby0JBG2JydJAsXn+acc2w+f2pOtnFW4Yem15acrL6gmQdRQ2EimyT7sditfVfVVfDhOcjPCOYVWUEdRvbnJIPTKzzCGI2iM3JASXr\/675LiRwcDEuNFaSpms\/paYWa+7D0awt4EPw\/xc4ifA\/yMh4A\/+A0ncB6XH936cokR8jH83roKmJk45dlcL\/rv\/E0o1Y0FJyDRgRiN3RFDXFv53+J10snMLddt\/NtcBnj6C5aoVgI44W\/jw8b8ugar8IYZ1qMOqi3tw6cvQvQtQ7bkLmhpNNmwK1CTnUwwMrusHW7gK2Y\/onKbv3jLXPA0x+owK7OEsq\/ozmKRFVzpS2nY+rUld5UIXTfpDl0lVPDaaS4OpmMxxS9lZOgtKH14AsHbhKGhfi+GqMD6KbldGPxwXH1r+OTbK1kLXMfF2xDwq0onCF0BURdeIyqExoa+VI\/AbaWNxwbTvScL9+mGtPFqVMpn+pVYCno1+enxMUUZnkPoVn+f3fcolZgvGtLxwYFH+9mn1UyhChbxV6Y2gldpNr85bfRNbUnQK5WPsUBzhZhMq\/+bNwDkVUSNyUPXpgGM14+XNOKU1qN1kzrIE4mHgqSOt19KkWLWHR2hiUNozbE859n0DKvNuUTVOtY75GhpqT3EaKxb356h8kz18PtRmfxvQGiMEu7bHY3qmfUq9BTUvn1Qq\/db9t448FhE3Oi9KJTcrf3muDhoSz40737jSTvDfc39wm0fQ2yyeCtRy79DI3ToadIylAgGA39udW+kAmukBe\/Rt72\/AVBLAwQUAAAACAC2ZG5XCcVgBpkBAABtAgAAMAAcAHN1Yl91MTU4NDc3Ml9hMjMzNjM3M19wMjMzNjQxOF9zMC8udm9jc3VibWl0LnR4dFVUCQADl9pTZZfaU2V1eAsAAQQwAAAABDAAAABtkVFvmzAUhf+K5adNijzbgEmo9pAF0mxaQkpIqSZLiBJTWQFcAaFpq\/z3GdNpmTTJsuzP59rnHr\/D+3Axj4L9GnrwncNOVoJDj8ON6gGxAcXUAoR6luvZ9LkC213M4YTDQpUH0Rjli2qOhp1a0ciDYcSZ2q5LDc7a+oNSy2I2mRoqqkyWhqremXVvd0fbqZad0xc\/1vTb66pmy5\/q\/IvdBUm2S\/YkEf5D\/tWU9qJppap1sTbcqzxXdSGf9Bbrw1I+fqz0u+OGQ2zq2ryRz117Tbqs6USTq4P4Qy8XOIG7eO8Hm3iMZBXH23S\/C6J0fquhEa7VmyzLjHP+xUEYfEpkfVAvLdjEgGCEb4AGzL4B52Fqeo\/gGcKfwa3Ij2ooophgPQhYykYU6jwwQrTG2IqCdRgH6dz3ozFNlyKLoKmLXOtasAqH3\/DqU1n+hdswGj1Sl\/1z3dDCtdr\/HgWLOP3vqen5IV2GUTKP\/MAfVqMVOkVUt0gwQ4xNwGCNzZAz01SHp7O7X6Rd9qSjK2SdlaA9PVayHf4LXn4DUEsDBAoAAAAAALpkblcAAAAAAAAAAAAAAAAmABwAc3ViX3UxNTg0NzcyX2EyMzM2MzczX3AyMzM2NDE4X3MwL3NyYy9VVAkAA5\/aU2Wf2lNldXgLAAEEMAAAAAQwAAAAUEsDBBQAAAAIALZkblf56iHR8AQAAFcTAAA8ABwAc3ViX3UxNTg0NzcyX2EyMzM2MzczX3AyMzM2NDE4X3MwL3NyYy9DdXN0b21lck9yZGVySGFzaC5qYXZhVVQJAAOX2lNll9pTZXV4CwABBDAAAAAEMAAAAOVY32\/bNhB+919xNVBMjhc5c5o+2EmwLC3QAlsSIHsr8kBLF5udJHoklcRb87\/vSP2iJDp2iu1pejFD3h3vvvvuSGZycDCAA7i8henJTzP4wDSDWy3zSOcSFbAshotkKSTXq1QZyRspvmKkYTqDGybplybN\/O\/XH65ncCnSdYIa4TJXWqQor2WM8hNTq7CU+5nleiXkzCrYiVyhzFiKzpQSuYxo+8JowpWGDU1BNb9CiSQ4GQx4uhbkxVf2wEKFUU6ObsLfUCm2xA98iUrP\/TJX4jaPVnVsH58iXGsusrZ4rnkSXkjJNr9yY2owWOeLhEcQJUypfpTw9wDoW0v+wAiFWvPLHWi2SHDeWuaZhixPrbbqL1mNS7ZmETlMe5v1icmX+ShnIlM2U0KCuAe9wsKrsBIo0IuqlBiBGO9ZnuituqVqZeFzxgkAlvC\/EBhk+NiOGJiJDx4JQGuCyWWeInm+JlMYh21rkyLAAr8ecoGJOCqDHZU4mo\/fQ8DVjeQpBvW6K2A+CxWcWRcb0Cvxu3kt\/AyYKNxLe4n6Cp90Z2fXVjWqc0g2jur1Vvpoxf4dJpgt9aoQeh70ck6bGjQuRYwB1SHPlqBGBK4Ujwq2cdYJp0V9iIufs858SLt8JgKwLMJgePvp4nB68n44aiJbbDQSZXn2Cw1MVIWhsPgJlDFgl4KRo1X6a5Svc73OdQlpMR+U1kamiurkUsirMl6SblTDajYYzRtxR7QevvXWScWcWuwUjrqkqdfGZ10bTYrroURqiVmtVGewU5bt4iuVTHG0K6eumSV\/wAxM\/\/NqZnmSmED6FriCTGhC0K5Z\/\/etN8Oyil1m530I1kLVKMHZmfWui6rjuBfHTspdwltfOgm0gX2pFO5eu2s9vqdOZ3sMt0VKP6fQsR0q6nPEN+Djcdd+Gz86Q4rBGQStlVHPpoGaO0XiQhjinzlLVFCZM8JXNE9V1d3fibGSbtt89mHdJW8Dzy7imurtxGwyJ\/Yi24PgsbEQdCy8mmfRy+n28svhNaUnajDtEMskpiD\/m1fv8QoOTya3G6UxDQU1Ner0mU4y6rl08BovhzB2XaS\/hsC0na7sf2dB9MTap1sw8gbWZS+L4yByROuTbjxueLSjA6biAe1F8jXNcP5iN2yrxwJV9oMGfKLA9u6BhWPf3Qb9eS2jjViSYPxjsQeZn5mE+rrbf9xIG28pO7tbYXU58TXAbrTBUCVCzyxVff2tYBLfyk+fTYNgNmHDjjnvnW2rPp2JmK71pmelf2\/zGmjpHZg3hhtW0zX+xwdR3QUOD+e9xRKAXe6U5df16F8+xpyWQ04v0L52Ks\/Uvpcnk60iJQ4YtS+t91vTDyeEYbExPSLMHT+tfVjDuSFP6rv9N0+O8nXYfQvRlOHeFL59g3J8PPJTMJ23uwVhDnZjujS\/d9YUNeBoBQGtd9MdMaq8o1l\/7t3MR4vqWHC\/hUT2x7xvYeq1YC7jx\/sbOd5qZLrTiMOwxxWnF2DwpnpoGty7UFTgE3YG9JMtleHZe2sDK8Xf7VEDblKdpckkpre9THlG7zTykFUcO4dj80SwvGvxbCFEgiyDKtQXaPaWWEaR9h5OpS\/31DLQC6ex+QQ2kf6+91T0PRMNDQxi29HmXh+2+7ELQi1zbGFYVnl9Nzptta5zeghTXdpVXwPQK65C5587ZPR58A9QSwMEFAAAAAgAtmRuV9tAxoPSBAAA5BQAADsAHABzdWJfdTE1ODQ3NzJfYTIzMzYzNzNfcDIzMzY0MThfczAvc3JjL09yZGVyU3lzdGVtTW9kZWwuamF2YVVUCQADl9pTZZfaU2V1eAsAAQQwAAAABDAAAAC1V01z2zYQvetXbH1IKSuhmkxykeNMUjuHziRWOnZPmRxQChaRoQgVAG2rHf\/3LgCCAkhAojMtLxKBxX6+fQvOT08ncAoX1\/DqzcsFXBJF4FqJplCNoBJIvYIP1ZoLpsqN1JJfBP9OCwWvFvCFCAWvcVGv3ywvlwu44JttRRWFpVhRcb2Tim4+8xWt8lbsPWlUycXCyJuFRlJRkw31liRvRIHWrc6KSQU7XAK3XlJBUXA+mbDNlqMT38kdySUtGvRzl1\/x66YoO7c\/PhR0qxivzyaTbfNnxQooKiLlwEf4ZwL4bAW7IxjCr1QpKi4aqfiGCiP8e0MbClz\/\/YRenQXyrFZQkC0p0IebErNX8mo1FDGn5SWtyI4mt5f1DdvQ1O4FqQtaxU6r6CnFFamMRavVCthU6P01VUvfq2zapkI\/giIU6pjbj2lF1v+0Hj++A2pcoGlFYSqiqm6C6GOq+vkZqkpiwbmq4ZD0co+VVutcd51+sPN4LU2\/cQH8FlRJLTrzVsDJ\/VYzxUjF\/qZAoKb3Q\/TqXu0vhkrmfkh90SyKXz8kVTKZDyTgPIX67kyXBJTVrqeymcUtTGPqHBRR5S\/RfQux5LYDTkRAxc+FKNkLYE17RXU1s\/yFjImkJduyBVHDPRIUbqzZHa1Bs2B+oGLIy6xeY2cbfVn7qk8935OD9s2+Yk1RrTDeTjEEwe8lpLgRyzzpwtWnMfdNpQvWFS9nNVK1ygZRZNYFz3xgenrmab6FrNX80zm8eOnDSz8WjzlvVI4EVquqzk4+rFZ0tYATmJlYPTR4faZ39hu6JN1LVxdbFHRBR2C8BSaBElEx\/KtKUgNOEEFbHn0OhZtmuiu7Q56yeRCYHzW89RKHJPGZPGTT3LHFpSeZTftJ0MZnszBMrd\/g8l2vruFR\/QTt0ddj9IdAnp23ql+EqsODj0ArSZPmbLf1rT1GS9VUVVCqkYWqcJyFye9ewqb6S3MJJjwAL4ZmauCBsZ9nL8dOxciKHUx5Ot3HrHhZimU\/lfl91v\/T3h3Xm\/0B6Md4RXRYiUkYkuaF33olW5cUpwea1bS18\/vwEFO6\/r2iDza\/2RN5EAHhpVB+3GzVblj9Y7gO0emcWtnXkRiNgTTU9P9CdZytHwbsQZA5LLRAG7picRUBX0p0FAT\/2K5IC0DXE6Yc7ppmiemWC\/O2H+HHcdkYzUvXc8NJjm16+dTpHQetxAsjov4cbyuIBB+pSYDyAS4xb1m\/vTszWrdWOGaUm5RiqAuoOUgMBQeuNX2SGOupnjqs3fER\/pzAreAbs8IPQNdIKm5Phtk3W+\/NjmKJJIwZ89ixg7p6desaxOiyEGnZuX\/sLHVK0A2\/o4Na6Sd2qej346iLlfs7P9XR93P11rbIs2eHs\/3OpjLGD5FAjsHK3uXxMr8ICk\/sPW7hl24YvvsQCAjJv1w8vSgD8B4bdsaFHyWV3ngxuuy083jlSRQSaPz6rU1UnxK8797DtwR\/W0dmvjSZ+YDCFnI3ZZlXtF6r8gzYbNZHRtdo8iv7pj8dYowTM78\/tWd\/A45Mg4Lpv1Pok8\/jSMbpU4FBXoIOn0poHaoDQvMtxupuP2iPEsLxJurUxeerjtazOH4CrDiV9c8K6AO6N5b0w1aMdqwb+M6n\/af54+RfUEsDBBQAAAAIALZkblfkP3sfVwIAALgIAAA4ABwAc3ViX3UxNTg0NzcyX2EyMzM2MzczX3AyMzM2NDE4X3MwL3NyYy9DdXN0b21lck9yZGVyLmphdmFVVAkAA5faU2WX2lNldXgLAAEEMAAAAAQwAAAAlVVNb9swDL37V3A51E6apEiBAUMybx3ayy5Lhva4i2IzsQrHyvQRYCjy3yfZXixZcrHo4g\/xPZJPJEUPR8YlvJITmStJy\/l6+4qZFKsouptMIpjA4zPcf1ws4YlIAs+Sq0wqjgJIlcO3cs84lcVBGMsNZwYL90v9ZX48ECULxutXJZBX5ID1h2CKZ5pjpr\/uoig6qm1JM8hKIgQ8KiHZAfma58jhLQK9jpyeiETjn1Z7MEQrZ4NWEpgBbEqSYf5CBw2esKQn5H\/CJkcmvlc\/FSq9FzW7TWxOVIkVxzTkexr2N27TMUsWVMwNAaRWPpedHqE2CqZnFt1B4rmCNIXZwnboUru2fXK4hU+dgzNgKfAqKl\/lmsjNsRMbTLCN3bmR\/WGt4ZzmaB9CK7tkzUtip8dR12UFI+eg3kZw60Rt1sjIncZ6qxZeP+JfcRwynPZ1SQ3I02oQaKvQQR29guBOmBpl6eSbx+fYEa6VytRfxg5HwvGFJW5PMVkgN9o5JTRwoJ8bc3+nX1vtASy8unmH\/MuV5DOfPWiXBHvIScX6\/xUWsDTd0q\/U92pxy1iJpAL8rUgpkmZuArMD\/5e46UW90camR2iveT8kTJ+XkKTKkO3cUTO+4HbajQV0j1QWROomcg96DGzV7w9vrqQ11tPk5sartOCM6cDOTgBud3uLs34FAO1VNG8VboZtjTOv40vVBybEHuUPbRMaEN2s9RtGw9auDiGG4CAeJrN1GaTz52WQcHMRLMRkX14+xYnRHEQoqP+7q66Y9WHHVvDuVeu5ci6GQFbn6C9QSwMEFAAAAAgAtmRuV9iqeW0lCAAA4iwAAEMAHABzdWJfdTE1ODQ3NzJfYTIzMzYzNzNfcDIzMzY0MThfczAvc3JjL0JldHRlckN1c3RvbWVyT3JkZXJRdWV1ZS5qYXZhVVQJAAOX2lNll9pTZXV4CwABBDAAAAAEMAAAAN1aS3PbNhC+61egPqSSXUm2O71YcSaJ3ZlmprXTOD1lfIApyEJCEiwB+pGM\/3t3wRcAgi8nTZvoEMXkYrH77eJbYKHl7u6E7JKTC3L4y8EROaWKkguVZoHKUiYJjdfkRXgtUq62kUTJ16l4zwJFDo\/Ia5oq8jM+fJo8w6+356fnR+REREnIFCMnmVQiYul5umbpnxnL2AKkUPA5zdRWpEd6hH6QSZbGNGLGIymyNAAbcq0hl4rcwyNSPt+ylIHgcjLhUSLAlPf0hi4kCzKw9n5xJi6yYFsZ\/+tdwBLFRbyaTCZJdhXygAQhlZK8ZEqxtGks+TQh8ElSfkNdb95dEoHfv4NVq3ax36jcEkWvQmYL8ViROIu0jASD8N0SI4Gf8ou8YRCEmKitD0pbdpmrz91yLb1m6rw0djor3MJPmk\/gePIwwB4w\/oqlRGzywRI80s\/\/7jENHQdzzkrffeYYwBTmOPZAhsVS56jQJuDEOpSLUiBPmaBMRBRYsw3NQtU61vH1VcwVpyH\/yAglMbv1REAvjka4O5xvS7QpohLQhAaQtyYgVWDIcdOGd+WIy1U1QKeaTxgtm1ZT1AMqrGHQfkv4CzR5DEtUFWgEhfLcxIUD3vMikmmdMDxesztCFbnd8mCbw17quKWy0M7Wq1JHMXZ+QPjGWgIQ1ixck1gocsWqcT05l4tNLUxIMAPFqbiVpI0rIBYVVGDG1IDruI7OImTxtdqakTPSeX5Qw\/1gq9PhWsB6mAb47xnw33Q2Iz9AALMwHKevMm1vr34fAB2q10K+ivNEq+2fkwMjDSpX3lkSl5AVwcqwGZAMRYAJZooho1p+aRlIKPRgYvlQZVXxubiXikULkakFcGOspjsnWZoyXA9FqOQR2TEsxc8Glq5eM1xnLXw9NUiD8L09FzrvVLXT\/HJRcuQpC\/kNS+\/fcowF2SM7jekfOj0I4+lsRXaLFCw\/eaSTDCLtaCuiCpB5w2oCNhqs8UB9EZAeWi3W4NQTIkpWciUCiUje8uivBLNotpr4oQCCAL9hDcMoQbbAbhph472h2QbfLTcwZxvxQfGQSHhizbRRJEsqiktoSiNtMJITfHNNGEUdpGlK7wkH5CUERwcphL9jlyGRS8uxNncZO4UCjwKgmUtKaMPTYrV5Mqvyz8ksHFpHF6QuF1gwacreCuOFVo9sQZbk8HKG6\/rAncmmVYh4Qgx6dFTY6d8mZSlA44YNc\/jOejlrU4HqYT60u0vE0Y2hWE18iBfxqiZfHs68EehPwLzypiwSN8ypmVCn9JMtv94y2CFAwmDxuiebVERtezFfZa5U5tN0VVI7zmsW\/kHvpoOKaL2Ilx5O2MlVwR4oDNl6x4TVrrodaY4Vs5dBAYFiKo2SgVDhrKci7ruBnx+YBjq5L97kwTq2NKxazSliq83ZVqcFy6byvzmN5QOm5UTGvsHkSnNyyxa7vrcC7Vvl1dv53FvCSpN8haBjg2EHrgP3fd++FW2pnkoefzgVt7EWHVhCX2xUlcvfVPXUxbNBJnUQWiglxfOxBAOgHiFeVYHLj3RsTa7udVlbA5DNauctUjeCr2vwu+rUs2Mzy5CU\/cvZX7Fw+8k2eBo6BKNQ3x4xdsP4PgU6tAUOWxcrAOEpM20rNYKxJNiy4AN6k88D1R3T108hdoHVAy5xYeEI8uSJW118xRe9zWvuvLEcwXpngaB0X5FzdI+ud35xrQsPC1lqi1RJ4bGtEWnCQsm+LGwN1DrSqzPeOu9GhLtAZJTZua+Dw63Fh8c71\/6FAl6G5V+I+GciNybiOPGQPbCVT2DRkDGWSb021UB8BXvmTYOWS3lLE82Y2NXSwt92+rnmPRri+ReKuQMxTvD98PlXRteTwR4SGU0VQ8I0OFTjw\/WIkA0MW1fonPCNxLBZqDwgNunEj6KPUnpg9NHKZ+PYTi8WkD5z6937Q8+ZXm\/XrzIFG23dzO485Uf0jkdZVJ3yRxzrB+roOOjDwSU\/6H9qHDfsQ26Xw9VOSrfLymaFPoHjvopFCfwJJy6Aose5NGOlHnv4imwopjHmcodzV0KEjMYw7Fcc1XkFpdvYfd0Zz61YCaDd\/RvTlnmsrsbVh+Qf2bBrNtu9Vi\/t5KjS6xrOlKCVRoOvJjGxphcKjrbXetyQTpLjRH2DohUMdEUvNE1MvV7JhAV8w+FYjBM4zbWVFyO9b3UurXKtXMY\/qqGxs4cWbZ+RaA3sgbxkG5Gy\/6r7Md2Bf11Zg6210GxUj6Tr9U4R\/7zZSIRuwB6hDU4y+czARpE2nyiwv22Ux9FG46b8q7V\/aLX7iuy2Ti61bOd9YVdjtEgrabRDvZcyBQZoldF3NMExbIPtAl6d6xeneY+4VmEKVrp8\/dWBqavbd99P5lrge\/uqPeSWJWta\/OJBuEaXv3c4aWwNHJZTAi+mcEgHP+mmXz6dSUs\/5T9uyYc\/mqO8C\/ccNlw8puHYtacX7hm7zccRHFjaZ17gDOPFsenVm1sNirFme+iEpHGZahOEjU43T3gpwsVX+vA1sOzgjW5uNeJg7dwLgcvemU2\/zYk9F0bV\/t1ipcr7+ihk6HlG9vGYajwxgr48HDeFlsjvCLtM+DR8QNst+SC+\/H9ndOGf5Vpdt+pNnHQq6YbfAZ1RnYYLAucCoR\/Jxt6reblRbsdt1vP9vs9X69quPz7vFrO8QDm2LlDmnj7TgAvJrvt0z3F5f9Ym3HOZh5\/H3Bq2kIHPrv59VON+p0X5N3pN2tve8F+VGvnUSZCtzGhQ4nAubCXB4ezX+VOKxlZp8jD5B1BLAwQUAAAACAC2ZG5XVN3SguMFAAB\/HgAAPQAcAHN1Yl91MTU4NDc3Ml9hMjMzNjM3M19wMjMzNjQxOF9zMC9zcmMvQ3VzdG9tZXJPcmRlclF1ZXVlLmphdmFVVAkAA5faU2WX2lNldXgLAAEEMAAAAAQwAAAA1VlLb9s4EL77VxA5FE4Dy0mAvcTtokWyhwK7TXfbPRU+0BJtcyuJXpKKmy7y33eGepikaD2StEBzMWIN5\/F938zI0vzlywl5Sa4\/kstfLq7IDdWUfNSyiHUhmSI0T8jbdCMk19tMoeUHKf5hsSaXV+QDlZpcwJf4\/afbm9srci2yXco0I9eF0iJj8lYmTP5ZsIJFleEbWuitkFfmhPmiUEzmNGPWV0oUMob4pdeUK03u4StSf79lkoHhfDKZ7IpVymMSp1SpQFjy34TA307yO+rn9XlJBH7+Dv4XjhnPNcmLzFipxcRcmyNU+Fd\/kDeSAUw5qT70lqEDBOue\/IvBXft5GaLM109kw\/Rtncv0tMoa\/yrnXqIPI3KCQlZMErEunaiOrLBuyOR9XXooE73lKrLACaYDSsiV0ZEwkTEPQ1FUG5TUxrVg0CBha1qk+uhZr9R3Odc8pSn\/xgglOdu7oBIqJb0ne5CucUHlpsgYFLgDVyyJhpJjZDRFZGK6ozGQa4PS8EJet1P4XJ9YLpoDDXJw4PwYeiU4PIfO0FVtceW4jIhMiYDion458DxhXwnVZL\/lcQlN43tPVRWVJT0yKc2mLuQxQjOZNMXyNZlaBb8+wBWlLN\/orQ2lpbHZxQGwh0kbu7Ozw\/U4Ukx\/EOpdXjJ1iDcjF6eLNlOfHYsl8BAvrJShtlTESKdttvDLMjZAoV\/Bx3ulWRaJQkdATa6nJ9eFlKi7GmV1RU6svPBvDUo3EuNGFfDxypo\/hJ+d+WGCoQ4l8mVUT5QblvI7Ju8\/8YxBP5+Rk1b4h84K0nzq2VcsAQRBmkZDML78Zyn94WjGZcmOJnYCO1btefb3Dsm3\/FRwgMWxfoYRp7CPRcKMC7JrGnRHJc2Md9PNQsFQEzmErIYWzjAOyCgAz4CYwv+53984IeqzbsdaG61KvqrGtGpTISgac3gVULRfnsc2Hj2gD1bLCKc6leyTsC4Y99iRZE4ul6fYOxd9rAINJ5h0xvMNKXa+bN3ZAyd3xJowXkT36DErxwHWMuyYN4Kci6fHXKB7iId5d5l4vpE5S5oWQRW9TfD55WmQsH65lutHskzcMW9B1Nt0yzdbBluvWT9rKTJzJXDnE1pDjcsyTNe6cXlOWPoH\/Tp15BsSTmkHSztNWXLitLOzlToknxdpGoSwwaosz5SAGsXC1lwCLixleLNhWc2tBeIpV\/xVQm2L73wZWl3nrkLdTXa0xFCvNVdns+Bwr5MKjcuOVepCZifu6fjcEmcwl8MiPl8cRX7FNjApFc+\/IPyJ2OdHEEeTG7hs4nZsqrdr3Wjs51pSQd7avS0Z7BEFEWGPICjNXip\/JrCErO7NOjqAaW+p4HK5Ezw5IBzaL22gK86iKGr1Jkb\/9bUlYJhkQ1bFe0HiLU8Tf0+UyISXF4qMrfHu\/RLqxMhn5MIVoYRR5xpcLo61MmAbWCHH1JvBWUiZxV+w7jIOLHrsIVfGNjoH5+bAErsbT5AXL\/zNEdrDWG25fmeD9m+ZlcG1DKP2tLWJoWyvvTGMv6daq8\/L6mlb0HOGt\/WF9GwajVbpdaoEZrhizws5IP4YyHMRRL1D151CM4IfobMKz1E1l0CN0JlJarTMTJgROivTei6h1Wr4Hkp7IujDlOaDPl5omPSQ23+nB6CaIWeccoZoqP6ZuWKwrBlZCbhZHbYRDgz8gGJmw6pBJszCwaew5rhfxnzetpn89B3TyvDR7My+o9Yc5DFkDzlo0sfNz7U0fzAtga4JTMwBc7H\/QdogfgdxPJzn8Vw\/hu+hnHfx7nE\/koD23cAgBoLzL0BBYAaGOQjOwR4SQrPw6Sx0zESHhjpjhwd7J\/c8zQm8EKp\/vLgPF8c8xnmsr9b7BMW\/sdDrpt43TdWLpPrmtv1OBG91WbaDf+EXfC50T1GyYLUf9\/iCrCmKHpXfUcxKiJTRHI79hqc6azJvEPqewpkjq0LDL3JMv\/u5XEa\/8qzIGgj6GRzro+PR3Ibp+tGcV3H7uRbU+zD5H1BLAQIeAwoAAAAAALpkblcAAAAAAAAAAAAAAAAiABgAAAAAAAAAEADtQQAAAABzdWJfdTE1ODQ3NzJfYTIzMzYzNzNfcDIzMzY0MThfczAvVVQFAAOf2lNldXgLAAEEMAAAAAQwAAAAUEsBAh4DCgAAAAAAumRuVwAAAAAAAAAAAAAAACcAGAAAAAAAAAAQAO1BXAAAAHN1Yl91MTU4NDc3Ml9hMjMzNjM3M19wMjMzNjQxOF9zMC90ZXN0L1VUBQADn9pTZXV4CwABBDAAAAAEMAAAAFBLAQIeAxQAAAAIALZkblcGDtL8gQYAAD4bAAA1ABgAAAAAAAEAAACkgb0AAABzdWJfdTE1ODQ3NzJfYTIzMzYzNzNfcDIzMzY0MThfczAvdGVzdC9QYXJ0MVRlc3QuamF2YVVUBQADl9pTZXV4CwABBDAAAAAEMAAAAFBLAQIeAxQAAAAIALZkbld0I12PhQkAAG0tAAA1ABgAAAAAAAEAAACkga0HAABzdWJfdTE1ODQ3NzJfYTIzMzYzNzNfcDIzMzY0MThfczAvdGVzdC9QYXJ0M1Rlc3QuamF2YVVUBQADl9pTZXV4CwABBDAAAAAEMAAAAFBLAQIeAxQAAAAIALZkblcW3rhyogcAACQiAAA1ABgAAAAAAAEAAACkgaERAABzdWJfdTE1ODQ3NzJfYTIzMzYzNzNfcDIzMzY0MThfczAvdGVzdC9QYXJ0MlRlc3QuamF2YVVUBQADl9pTZXV4CwABBDAAAAAEMAAAAFBLAQIeAxQAAAAIALZkbldLUEjMIwYAAJEYAAA1ABgAAAAAAAEAAACkgbIZAABzdWJfdTE1ODQ3NzJfYTIzMzYzNzNfcDIzMzY0MThfczAvdGVzdC9QYXJ0NFRlc3QuamF2YVVUBQADl9pTZXV4CwABBDAAAAAEMAAAAFBLAQIeAxQAAAAIALZkblcJxWAGmQEAAG0CAAAwABgAAAAAAAEAAACkgUQgAABzdWJfdTE1ODQ3NzJfYTIzMzYzNzNfcDIzMzY0MThfczAvLnZvY3N1Ym1pdC50eHRVVAUAA5faU2V1eAsAAQQwAAAABDAAAABQSwECHgMKAAAAAAC6ZG5XAAAAAAAAAAAAAAAAJgAYAAAAAAAAABAA7UFHIgAAc3ViX3UxNTg0NzcyX2EyMzM2MzczX3AyMzM2NDE4X3MwL3NyYy9VVAUAA5\/aU2V1eAsAAQQwAAAABDAAAABQSwECHgMUAAAACAC2ZG5X+eoh0fAEAABXEwAAPAAYAAAAAAABAAAApIGnIgAAc3ViX3UxNTg0NzcyX2EyMzM2MzczX3AyMzM2NDE4X3MwL3NyYy9DdXN0b21lck9yZGVySGFzaC5qYXZhVVQFAAOX2lNldXgLAAEEMAAAAAQwAAAAUEsBAh4DFAAAAAgAtmRuV9tAxoPSBAAA5BQAADsAGAAAAAAAAQAAAKSBDSgAAHN1Yl91MTU4NDc3Ml9hMjMzNjM3M19wMjMzNjQxOF9zMC9zcmMvT3JkZXJTeXN0ZW1Nb2RlbC5qYXZhVVQFAAOX2lNldXgLAAEEMAAAAAQwAAAAUEsBAh4DFAAAAAgAtmRuV+Q\/ex9XAgAAuAgAADgAGAAAAAAAAQAAAKSBVC0AAHN1Yl91MTU4NDc3Ml9hMjMzNjM3M19wMjMzNjQxOF9zMC9zcmMvQ3VzdG9tZXJPcmRlci5qYXZhVVQFAAOX2lNldXgLAAEEMAAAAAQwAAAAUEsBAh4DFAAAAAgAtmRuV9iqeW0lCAAA4iwAAEMAGAAAAAAAAQAAAKSBHTAAAHN1Yl91MTU4NDc3Ml9hMjMzNjM3M19wMjMzNjQxOF9zMC9zcmMvQmV0dGVyQ3VzdG9tZXJPcmRlclF1ZXVlLmphdmFVVAUAA5faU2V1eAsAAQQwAAAABDAAAABQSwECHgMUAAAACAC2ZG5XVN3SguMFAAB\/HgAAPQAYAAAAAAABAAAApIG\/OAAAc3ViX3UxNTg0NzcyX2EyMzM2MzczX3AyMzM2NDE4X3MwL3NyYy9DdXN0b21lck9yZGVyUXVldWUuamF2YVVUBQADl9pTZXV4CwABBDAAAAAEMAAAAFBLBQYAAAAADQANADAGAAAZPwAAAAA="

content_2 = content.replace("\\", "")


content_64 = base64.b64decode(content_2)


with open("temp.zip", "wb") as f:
    f.write(content_64)





