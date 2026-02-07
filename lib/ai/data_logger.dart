import 'dart:io';
import 'package:path_provider/path_provider.dart';

class DataLogger {
  static Future<File> _getFile() async {
    final directory = await getApplicationDocumentsDirectory();
    final file = File('${directory.path}/ad_click_dataset.csv');

    if (!await file.exists()) {
      await file.writeAsString(
        "age,ad_id,ad_title,clicked,timestamp\n",
        mode: FileMode.write,
      );
    }
    return file;
  }

  static Future<void> logInteraction({
    required int age,
    required String adId,
    required String adTitle,
    required bool clicked,
  }) async {
    final file = await _getFile();
    final timestamp = DateTime.now().toIso8601String();

    final row =
        "$age,$adId,$adTitle,${clicked ? 1 : 0},$timestamp\n";

    await file.writeAsString(row, mode: FileMode.append);
  }
}
