# CardMetadataHelper.ToString - метод
Преобразует объект заданного типа в строку. Объект может быть преобразован в
исходную форму методом [Parse(String,
CardMetadataRuntimeType)](M_Tessa_Cards_Metadata_CardMetadataHelper_Parse.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string ToString(
    	Object value,
    	CardMetadataRuntimeType type
    )
VB __Копировать
     Public Shared Function ToString ( 
    	value As Object,
    	type As CardMetadataRuntimeType
    ) As String
C++ __Копировать
     public:
    static String^ ToString(
    	Object^ value, 
    	CardMetadataRuntimeType type
    )
F# __Копировать
     static member ToString : 
            value : Object * 
            type : CardMetadataRuntimeType -> string 
#### Параметры
value [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Объект, который требуется преобразовать в строку.
type
[CardMetadataRuntimeType](T_Tessa_Cards_Metadata_CardMetadataRuntimeType.htm)
    Тип объекта, который требуется преобразовать в строку.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Строковое представление заданного объекта.
##  __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
