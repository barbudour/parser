# CardSerializableObject.SerializeToXml(Boolean) - метод
Возвращает строку, которая содержит сериализованный в XML объект.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string SerializeToXml(
    	bool omitXmlDeclaration = false
    )
VB __Копировать
     Public Function SerializeToXml ( 
    	Optional omitXmlDeclaration As Boolean = false
    ) As String
C++ __Копировать
     public:
    String^ SerializeToXml(
    	bool omitXmlDeclaration = false
    )
F# __Копировать
     member SerializeToXml : 
            ?omitXmlDeclaration : bool 
    (* Defaults:
            let _omitXmlDeclaration = defaultArg omitXmlDeclaration false
    *)
    -> string 
#### Параметры
omitXmlDeclaration
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что в результирующем документе не должен выводится заголовок XML вида <?xml version="1.0" encoding="utf-8">>. 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Строка, содержащая сериализованный в XML объект.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[SerializeToXml -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_SerializeToXml.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
