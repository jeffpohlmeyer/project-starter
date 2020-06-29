import LocalScheme from '@nuxtjs/auth/lib/schemes/local'

export default class CustomScheme extends LocalScheme {
  // Override `login` method of `local` scheme
  async login(endpoint) {
    if (!this.options.endpoints.login) {
      return
    }

    // Ditch any leftover local tokens before attempting to log in
    await this.$auth.reset()

    const { response, result } = await this.$auth.request(
      endpoint,
      this.options.endpoints.login,
      true
    )

    if (this.options.tokenRequired) {
      const token = this.options.tokenType
        ? this.options.tokenType + ' ' + result.access
        : result.access

      this.$auth.setToken(this.name, token)
      this._setToken(token)
    }

    if (this.options.autoFetchUser) {
      await this.fetchUser()
    }

    return response
  }
}
