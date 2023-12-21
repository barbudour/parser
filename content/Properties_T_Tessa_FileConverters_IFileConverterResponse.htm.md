# IFileConverterResponse - свойства
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
## __См. также
#### Ссылки
[IFileConverterResponse - ](T_Tessa_FileConverters_IFileConverterResponse.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
