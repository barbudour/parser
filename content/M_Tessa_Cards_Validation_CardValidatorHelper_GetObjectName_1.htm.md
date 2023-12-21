# CardValidatorHelper.GetObjectName(CardMetadataSection, CardMetadataColumn) -
метод
Возвращает имя объекта валидации, полученное по секции и колонке, которые он
проверяет.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetObjectName(
    	CardMetadataSection section,
    	CardMetadataColumn column
    )
VB __Копировать
     Public Shared Function GetObjectName ( 
    	section As CardMetadataSection,
    	column As CardMetadataColumn
    ) As String
C++ __Копировать
     public:
    static String^ GetObjectName(
    	CardMetadataSection^ section, 
    	CardMetadataColumn^ column
    )
F# __Копировать
     static member GetObjectName : 
            section : CardMetadataSection * 
            column : CardMetadataColumn -> string 
#### Параметры
section [CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
    Секция, проверку колонки которой осуществляется валидатор.
column [CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
    Колонка, проверку которой осуществляет валидатор.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Имя объекта валидации, полученное по секции и колонке, которые он проверяет.
##  __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[GetObjectName -
перегрузка](Overload_Tessa_Cards_Validation_CardValidatorHelper_GetObjectName.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
