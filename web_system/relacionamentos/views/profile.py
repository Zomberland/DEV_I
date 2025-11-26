class ProfileView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        context = {
            'usuario' : request.user,
        }
        return render(request, 'accounts/profile.html', context)
