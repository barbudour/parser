# XmlHelper.GetAttributeValue<T> \- метод
Возвращает строготипизированное значение указанного атрибута.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static T GetAttributeValue<T>(
    	XAttribute attribute,
    	Func<string, T> parseFromString,
    	T defaultValue = null
    )
VB __Копировать
     Public Shared Function GetAttributeValue(Of T) ( 
    	attribute As XAttribute,
    	parseFromString As Func(Of String, T),
    	Optional defaultValue As T = Nothing
    ) As T
C++ __Копировать
     public:
    generic<typename T>
    static T GetAttributeValue(
    	XAttribute^ attribute, 
    	Func<String^, T>^ parseFromString, 
    	T defaultValue = nullptr
    )
F# __Копировать
     static member GetAttributeValue : 
            attribute : XAttribute * 
            parseFromString : Func<string, 'T> * 
            ?defaultValue : 'T 
    (* Defaults:
            let _defaultValue = defaultArg defaultValue null
    *)
    -> 'T 
#### Параметры
attribute
[XAttribute](https://learn.microsoft.com/dotnet/api/system.xml.linq.xattribute)
    Атрибут XML, значение которого требуется получить.
parseFromString
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
T>
    Метод, преобразующий значение атрибута в тип T.
defaultValue T (Optional)
    Значение атрибута по умолчанию, используемое, если атрибут не указан.
#### Параметры типа
T
    Тип значения атрибута.
#### Возвращаемое значение
T  
Значение указанного атрибута.
##  __См. также
#### Ссылки
[XmlHelper - ](T_Chronos_Platform_XmlHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
