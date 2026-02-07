class AdModel {
  final String id;
  final String title;
  final String description;
  int clicks;

  AdModel({
    required this.id,
    required this.title,
    required this.description,
    this.clicks = 0,
  });
}
