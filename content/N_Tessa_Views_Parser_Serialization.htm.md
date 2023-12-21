# Tessa.Views.Parser.Serialization - пространство имён
Классы сериализации для парсера представлений.
##  __Классы
[ExchangeFormatRegistration](T_Tessa_Views_Parser_Serialization_ExchangeFormatRegistration.htm)|
Регистрация зависимостей формата обмена  
---|---  
[ExchangeFormatSerializer](T_Tessa_Views_Parser_Serialization_ExchangeFormatSerializer.htm)|
Используется для сохранения объектов в формат обмена. Сериализация объектов
осуществляется в поток.  
[LinkSerializationException](T_Tessa_Views_Parser_Serialization_LinkSerializationException.htm)|
Исключение возникающее при сериализации ссылки  
[ParametersWriter](T_Tessa_Views_Parser_Serialization_ParametersWriter.htm)|
Осуществляет запись параметра в поток  
[TessaExchangeFormat](T_Tessa_Views_Parser_Serialization_TessaExchangeFormat.htm)|
Класс содержащий формат обмена данными  
[UserExtensionsSerializer](T_Tessa_Views_Parser_Serialization_UserExtensionsSerializer.htm)|
Сериализатор пользовательских расширений рабочего места  
[ViewFilePersistent](T_Tessa_Views_Parser_Serialization_ViewFilePersistent.htm)|
Реализация чтения/сохранения моделей представлений во внешние файлы.  
[ViewSerializationRegistration](T_Tessa_Views_Parser_Serialization_ViewSerializationRegistration.htm)|
Осуществляет регистрацию зависимостей необходимых для сериализации метаданных
подсистемы представлений  
[WorkplaceFilePersistent](T_Tessa_Views_Parser_Serialization_WorkplaceFilePersistent.htm)|
Реализация чтения/сохранения моделей представлений во внешние файлы.  
[WorkplaceMetadataSerializer](T_Tessa_Views_Parser_Serialization_WorkplaceMetadataSerializer.htm)|
Сериализатор метаданных рабочего места  
## __Интерфейсы
[IExchangeFormatObjectWriter](T_Tessa_Views_Parser_Serialization_IExchangeFormatObjectWriter.htm)|
Маркер-интерфейс для писателей объектов формата обмена  
---|---  
[IObjectWriter](T_Tessa_Views_Parser_Serialization_IObjectWriter.htm)|
Интерфейс предназначенный для записи объекта в поток  
[IObjectWriterRegistry<T>](T_Tessa_Views_Parser_Serialization_IObjectWriterRegistry_1.htm)|
Реестр объектов осуществляющих сериализацию  
[IUserExtensionsMetadataObjectWriter](T_Tessa_Views_Parser_Serialization_IUserExtensionsMetadataObjectWriter.htm)|
Маркер-интерфейс для писателей метаданных пользовательских расширений  
[IWorkplaceMetadataObjectWriter](T_Tessa_Views_Parser_Serialization_IWorkplaceMetadataObjectWriter.htm)|
Маркер-интерфейс для писателей метаданных рабочего места  
## __Делегаты
[ObjectWriterResolver<T>](T_Tessa_Views_Parser_Serialization_ObjectWriterResolver_1.htm)|
Делегат осуществляющий поиск писателя объекта для типа type  
---|---
