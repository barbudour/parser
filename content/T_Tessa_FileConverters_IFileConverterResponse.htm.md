# IFileConverterResponse - интерфейс
Результат конвертации файла с возможностью получить доступ к его контенту.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileConverterResponse
VB __Копировать
     Public Interface IFileConverterResponse
C++ __Копировать
     public interface class IFileConverterResponse
F# __Копировать
     type IFileConverterResponse = interface end
##  __Свойства
[HasAwaitedResult](P_Tessa_FileConverters_IFileConverterResponse_HasAwaitedResult.htm)|
Признак того, что ожидание результата было выполнено и результат был получен
(успешный или с ошибками). Если значение равно false, то метод получения
содержимого файла
[Tessa.FileConverters.IFileConverterResponse.GetStreamOrThrow] выбросит
исключение.  
---|---  
[Info](P_Tessa_FileConverters_IFileConverterResponse_Info.htm)| Дополнительная
информация, полученная из результатов операции конвертации.  
[IsAcquiredFromCache](P_Tessa_FileConverters_IFileConverterResponse_IsAcquiredFromCache.htm)|
Признак того, что результат конвертации был получен из кэша.  
[Size](P_Tessa_FileConverters_IFileConverterResponse_Size.htm)|  Размер
содержимого [Tessa.FileConverters.IFileConverterResponse.GetStreamOrThrow] в
байтах или -1, если содержимое отсутствует или размер неизвестен.  
[ValidationResult](P_Tessa_FileConverters_IFileConverterResponse_ValidationResult.htm)|
Результат выполнения операции. Если он содержит ошибки, то метод
[Tessa.FileConverters.IFileConverterResponse.GetStreamOrThrow] выбросит
исключение.  
## __Методы
[GetStreamOrThrowAsync](M_Tessa_FileConverters_IFileConverterResponse_GetStreamOrThrowAsync.htm)|
Возвращает поток с содержимым файла. Возвращённое значение потока не равно
null. В случае ошибок в
[Tessa.FileConverters.IFileConverterResponse.ValidationResult] или в случае,
если ожидание результата не было завершено, т.е.
[Tessa.FileConverters.IFileConverterResponse.HasAwaitedResult] равен false,
выбрасывается исключение.  
---|---  
## __См. также
#### Ссылки
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
