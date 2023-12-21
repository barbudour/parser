# Tessa.Views.Metadata.Types - пространство имён
API представлений в части связи со схемой данных.
##  __Классы
[InvalidTypeException](T_Tessa_Views_Metadata_Types_InvalidTypeException.htm)|
Тип исключительной ситуации возникающей при ошибке с типами данных  
---|---  
[SchemeTypeConverter](T_Tessa_Views_Metadata_Types_SchemeTypeConverter.htm)|
Осуществляет преобразование типов подсистемы баз данных и
[SchemeType](T_Tessa_Scheme_SchemeType.htm) в строковое представление и
обратно  
[TypeConverterRegistration](T_Tessa_Views_Metadata_Types_TypeConverterRegistration.htm)|
Осуществляет регистрацию объектов и зависимостей необходимых для работы
конвертеров типов  
[TypesHelper](T_Tessa_Views_Metadata_Types_TypesHelper.htm)|  Вспомогательные
методы для работы с типами  
[ViewResultConverter](T_Tessa_Views_Metadata_Types_ViewResultConverter.htm)|
The view result converter.  
## __Интерфейсы
[IDbmsSchemeTypeConverter](T_Tessa_Views_Metadata_Types_IDbmsSchemeTypeConverter.htm)|
Описание интерфейса конвертера типов данных под конкретную подсистему баз
данных  
---|---  
[ISchemeTypeConverter](T_Tessa_Views_Metadata_Types_ISchemeTypeConverter.htm)|
Описание интерфейса для типов осуществляющих преобразование типов схемы данных
из строкового представления в экземпляры
[SchemeType](T_Tessa_Scheme_SchemeType.htm) и обратно.  
## __Делегаты
[DbmsTypeConverterFactory](T_Tessa_Views_Metadata_Types_DbmsTypeConverterFactory.htm)|
Делегат фабрики создания конвертера типов под конкретную подсистему баз данных  
---|---  
[TableColumnTypeResolverDelegateAsync](T_Tessa_Views_Metadata_Types_TableColumnTypeResolverDelegateAsync.htm)|
Делегат получения типа данных ссылки на столбец таблицы схемы по имени.
