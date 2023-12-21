# CardExtensions.GetFieldNames - метод
Возвращает имена полей, с которыми связан контрол
[CardTypeEntryControl](T_Tessa_Cards_CardTypeEntryControl.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<string> GetFieldNames(
    	this CardTypeEntryControl control,
    	CardMetadataSection metadataSection,
    	out string defaultFieldName,
    	out CardMetadataRuntimeType defaultFieldType
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetFieldNames ( 
    	control As CardTypeEntryControl,
    	metadataSection As CardMetadataSection,
    	<OutAttribute> ByRef defaultFieldName As String,
    	<OutAttribute> ByRef defaultFieldType As CardMetadataRuntimeType
    ) As List(Of String)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static List<String^>^ GetFieldNames(
    	CardTypeEntryControl^ control, 
    	CardMetadataSection^ metadataSection, 
    	[OutAttribute] String^% defaultFieldName, 
    	[OutAttribute] CardMetadataRuntimeType% defaultFieldType
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetFieldNames : 
            control : CardTypeEntryControl * 
            metadataSection : CardMetadataSection * 
            defaultFieldName : string byref * 
            defaultFieldType : CardMetadataRuntimeType byref -> List<string> 
#### Параметры
control [CardTypeEntryControl](T_Tessa_Cards_CardTypeEntryControl.htm)
     Контрол, для которого требуется определить имена связанных полей. 
metadataSection
[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
     Секция в метаинформации по типу карточки, с которой связан контрол control. 
defaultFieldName
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля по умолчанию, используемое при отсутствии форматирования в контроле. 
defaultFieldType
[CardMetadataRuntimeType](T_Tessa_Cards_Metadata_CardMetadataRuntimeType.htm)
     Тип поля по умолчанию. 
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Имена полей, с которыми связан контрол.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardTypeEntryControl](T_Tessa_Cards_CardTypeEntryControl.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
