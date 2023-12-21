# XmlHelper.GetAttributeString - метод
Возвращает строковое значение указанного атрибута.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetAttributeString(
    	XAttribute attribute,
    	string defaultValue = null
    )
VB __Копировать
     Public Shared Function GetAttributeString ( 
    	attribute As XAttribute,
    	Optional defaultValue As String = Nothing
    ) As String
C++ __Копировать
     public:
    static String^ GetAttributeString(
    	XAttribute^ attribute, 
    	String^ defaultValue = nullptr
    )
F# __Копировать
     static member GetAttributeString : 
            attribute : XAttribute * 
            ?defaultValue : string 
    (* Defaults:
            let _defaultValue = defaultArg defaultValue null
    *)
    -> string 
#### Параметры
attribute
[XAttribute](https://learn.microsoft.com/dotnet/api/system.xml.linq.xattribute)
    Атрибут XML, значение которого требуется получить.
defaultValue [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Значение атрибута по умолчанию, используемое, если атрибут не указан.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Строковое значение указанного атрибута.
##  __См. также
#### Ссылки
[XmlHelper - ](T_Chronos_Platform_XmlHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
