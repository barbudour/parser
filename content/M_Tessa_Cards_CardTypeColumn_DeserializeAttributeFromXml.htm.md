# CardTypeColumn.DeserializeAttributeFromXml - метод
Выполняется для каждого атрибута десериализуемого атрибута.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override bool DeserializeAttributeFromXml(
    	string name,
    	string value
    )
VB __Копировать
     Protected Overrides Function DeserializeAttributeFromXml ( 
    	name As String,
    	value As String
    ) As Boolean
C++ __Копировать
     protected:
    virtual bool DeserializeAttributeFromXml(
    	String^ name, 
    	String^ value
    ) override
F# __Копировать
     abstract DeserializeAttributeFromXml : 
            name : string * 
            value : string -> bool 
    override DeserializeAttributeFromXml : 
            name : string * 
            value : string -> bool 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя атрибута без учёта пространства имён.
value [String](https://learn.microsoft.com/dotnet/api/system.string)
    Значение атрибута.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если атрибут был успешно десериализован; false в противном случае.
## __См. также
#### Ссылки
[CardTypeColumn - ](T_Tessa_Cards_CardTypeColumn.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
