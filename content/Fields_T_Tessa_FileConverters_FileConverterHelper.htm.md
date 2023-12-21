# FileConverterHelper - поля
##  __Поля
[CacheCardID](F_Tessa_FileConverters_FileConverterHelper_CacheCardID.htm)|
Идентификатор карточки кэша сконвертированных файлов.  
---|---  
[LightweightLoadingKey](F_Tessa_FileConverters_FileConverterHelper_LightweightLoadingKey.htm)|
Ключ в запросе на загрузку карточки кэша, который определяет, что будут
загружены только данные виртуальной секции. Укажите true, чтобы не загружать
другие секции.  
[OldestPreviewRequestTimeKey](F_Tessa_FileConverters_FileConverterHelper_OldestPreviewRequestTimeKey.htm)|
Самая поздняя разрешённая дата, когда выполнялось обращение к файлу в кэше.
Все файлы, к которым обращались раньше это даты, будут удалены из кэша.
Укажите такую дату по этому ключу в запросе на сохранение карточки файловых
конвертеров. Значение null указывает, что из кэша будут удалены все файлы.  
[OperationCheckIntervalMilliseconds](F_Tessa_FileConverters_FileConverterHelper_OperationCheckIntervalMilliseconds.htm)|
Интервал в миллисекундах, по завершении которого будет проверка граничного
условия в цикле ожидания. Используется при ожидании асинхронных операций.  
## __См. также
#### Ссылки
[FileConverterHelper - ](T_Tessa_FileConverters_FileConverterHelper.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
