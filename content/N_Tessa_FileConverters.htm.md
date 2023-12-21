# Tessa.FileConverters - пространство имён
API конвертации файлов. Используется для предпросмотра в Web-клиенте, а также
для любых других нужд, связанных с необходимостью асинхронно преобразовать или
видоизменить файл.
##  __Классы
[FileConverter](T_Tessa_FileConverters_FileConverter.htm)|  Объект, выполнющий
преобразование файлов из одного формата в другой.  
---|---  
[FileConverterAggregateWorker](T_Tessa_FileConverters_FileConverterAggregateWorker.htm)|
Объект, ответственный за преобразование файла посредством внешних программ, и
обеспечивающий выбор алгоритма преобразования в зависимости от формата
выходного файла.  
[FileConverterAnyEventNamePolicy](T_Tessa_FileConverters_FileConverterAnyEventNamePolicy.htm)|
Политика, определяющая допустимость любого имени события по конвертации файлов
для выполнения методов расширения. Может быть использована для замещения
другой политики
[IFileConverterEventNamePolicy](T_Tessa_FileConverters_IFileConverterEventNamePolicy.htm).  
[FileConverterAnyOutputFormatPolicy](T_Tessa_FileConverters_FileConverterAnyOutputFormatPolicy.htm)|
Политика, определяющая допустимость любого выходного формата по конвертации
файлов для выполнения методов расширения. Может быть использована для
замещения другой политики
[IFileConverterOutputFormatPolicy](T_Tessa_FileConverters_IFileConverterOutputFormatPolicy.htm).  
[FileConverterCache](T_Tessa_FileConverters_FileConverterCache.htm)|  Объект,
обеспечивающий кэширование файлов, преобразованных из одного формата в другой.  
[FileConverterCacheNames](T_Tessa_FileConverters_FileConverterCacheNames.htm)|
Имена объектов кэша
[IFileConverterCache](T_Tessa_FileConverters_IFileConverterCache.htm), которые
регистрируются в Unity.  
[FileConverterComposer](T_Tessa_FileConverters_FileConverterComposer.htm)|
Объект, выполнющий пошаговое преобразование файлов из одного формата в другой.  
[FileConverterContext](T_Tessa_FileConverters_FileConverterContext.htm)|
Контекст операции конвертации для
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm) или
для расширений
[IFileConverterExtension](T_Tessa_FileConverters_IFileConverterExtension.htm).  
[FileConverterEventNamePolicy](T_Tessa_FileConverters_FileConverterEventNamePolicy.htm)|
Политика, определяющая допустимость имени события по конвертации файлов.  
[FileConverterEventNames](T_Tessa_FileConverters_FileConverterEventNames.htm)|
Алиасы стандартных событий, для которых выполняется предпросмотр. Расширения
могут использовать любые другие алиасы для своих событий.  
[FileConverterExtension](T_Tessa_FileConverters_FileConverterExtension.htm)|
Базовый класс расширения для операции по конвертированию файла.  
[FileConverterExtensionFilterPolicy](T_Tessa_FileConverters_FileConverterExtensionFilterPolicy.htm)|
Политика фильтрации расширений, использующая политику
[IFileConverterEventNamePolicy](T_Tessa_FileConverters_IFileConverterEventNamePolicy.htm)
для того, чтобы не выполнять методы расширений, для которых в контексте
[IFileConverterContext](T_Tessa_FileConverters_IFileConverterContext.htm)
использовано имя события, запрещённое указанной политикой. Если политика
[IFileConverterEventNamePolicy](T_Tessa_FileConverters_IFileConverterEventNamePolicy.htm)
не зарегистрирована, то метод расширения выполняется.  
[FileConverterExtensions](T_Tessa_FileConverters_FileConverterExtensions.htm)|
Методы-расширения для пространства имён Tessa.FileConverters.  
[FileConverterHelper](T_Tessa_FileConverters_FileConverterHelper.htm)|
Вспомогательные методы и константы для API конвертации файлов.  
[FileConverterOutputFormatPolicy](T_Tessa_FileConverters_FileConverterOutputFormatPolicy.htm)|
Политика, определяющая допустимость выходного формата по конвертации файлов.  
[FileConverterRequest](T_Tessa_FileConverters_FileConverterRequest.htm)|
Запрос на конвертацию файла.  
[FileConverterResponse](T_Tessa_FileConverters_FileConverterResponse.htm)|
Результат конвертации файла с возможностью получить доступ к его контенту.  
## __Структуры
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)|  Формат
файла, в который выполняется конвертация.  
---|---  
## __Интерфейсы
[IFileConverter](T_Tessa_FileConverters_IFileConverter.htm)|  Объект,
выполнющий преобразование файлов из одного формата в другой.  
---|---  
[IFileConverterAggregateWorker](T_Tessa_FileConverters_IFileConverterAggregateWorker.htm)|
Объект, ответственный за преобразование файла посредством внешних программ, и
обеспечивающий выбор алгоритма преобразования в зависимости от формата
выходного файла.  
[IFileConverterCache](T_Tessa_FileConverters_IFileConverterCache.htm)|
Объект, обеспечивающий кэширование файлов, преобразованных из одного формата в
другой.  
[IFileConverterComposer](T_Tessa_FileConverters_IFileConverterComposer.htm)|
Объект, выполнющий пошаговое преобразование файлов из одного формата в другой.  
[IFileConverterContext](T_Tessa_FileConverters_IFileConverterContext.htm)|
Контекст операции конвертации для
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm) или
для расширений
[IFileConverterExtension](T_Tessa_FileConverters_IFileConverterExtension.htm).  
[IFileConverterEventNamePolicy](T_Tessa_FileConverters_IFileConverterEventNamePolicy.htm)|
Политика, определяющая допустимость имени события по конвертации файлов.  
[IFileConverterExtension](T_Tessa_FileConverters_IFileConverterExtension.htm)|
Расширение для операции по конвертированию файла.  
[IFileConverterOutputFormatPolicy](T_Tessa_FileConverters_IFileConverterOutputFormatPolicy.htm)|
Политика, определяющая допустимость выходного формата по конвертации файлов.  
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)|
Запрос на конвертацию файла.  
[IFileConverterResponse](T_Tessa_FileConverters_IFileConverterResponse.htm)|
Результат конвертации файла с возможностью получить доступ к его контенту.  
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm)|
Объект, ответственный за преобразование файла посредством внешних программ,
таких как OpenOffice или LibreOffice. Класс может также реализовывать
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable) для
очистки ресурсов.  
## __Перечисления
[FileConverterRequestFlags](T_Tessa_FileConverters_FileConverterRequestFlags.htm)|
Флаги с настройками конвертации файлов.  
---|---
