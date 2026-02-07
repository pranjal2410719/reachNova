class ClickTracker {
  static final Map<String, int> _clicks = {};

  static void registerClick(String adId) {
    _clicks[adId] = (_clicks[adId] ?? 0) + 1;
  }

  static int getClicks(String adId) {
    return _clicks[adId] ?? 0;
  }
}
