# Tessa.Extensions.Default.Chronos.FileConverters - пространство имён
Расширения для конвертации файлов в фоновых сервисах.
##  __Классы
[FileConverterPlugin](T_Tessa_Extensions_Default_Chronos_FileConverters_FileConverterPlugin.htm)|
Делает преобразование файлов, сохраняет их в карточку кэша  
---|---  
[FileConverterSettings](T_Tessa_Extensions_Default_Chronos_FileConverters_FileConverterSettings.htm)|  
[FileConverterWorkerNames](T_Tessa_Extensions_Default_Chronos_FileConverters_FileConverterWorkerNames.htm)|
Имена стандартных конвертеров
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm),
которые используются в других конвертерах.  
[PdfFileConverterWorker](T_Tessa_Extensions_Default_Chronos_FileConverters_PdfFileConverterWorker.htm)|
Объект, ответственный за преобразование файла в формат
[Pdf](F_Tessa_FileConverters_FileConverterFormat_Pdf.htm) посредством внешних
программ, таких как OpenOffice или LibreOffice.  
[TiffToPdfFileConverterWorker](T_Tessa_Extensions_Default_Chronos_FileConverters_TiffToPdfFileConverterWorker.htm)|
Объект, ответственный за преобразование файла в формат
[Pdf](F_Tessa_FileConverters_FileConverterFormat_Pdf.htm) из формата TIFF.
Обычно не используется как самостоятельный Worker, а применяется в составе
[PdfFileConverterWorker](T_Tessa_Extensions_Default_Chronos_FileConverters_PdfFileConverterWorker.htm).
Регистрация выполняется по константе
[TiffToPdf](F_Tessa_Extensions_Default_Chronos_FileConverters_FileConverterWorkerNames_TiffToPdf.htm).
