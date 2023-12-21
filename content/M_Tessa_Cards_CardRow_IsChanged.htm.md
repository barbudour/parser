# CardRow.IsChanged - метод
Возвращает признак того, что значение объекта с ключом key было изменено.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsChanged(
    	string key
    )
VB __Копировать
     Public Function IsChanged ( 
    	key As String
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsChanged(
    	String^ key
    ) sealed
F# __Копировать
     abstract IsChanged : 
            key : string -> bool 
    override IsChanged : 
            key : string -> bool 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому необходимо определить признак того, что значение соответствующего объекта было изменено. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если значение объекта было изменено; false, если значение объекта
осталось неизменным.
#### Реализации
[IStorageObjectStateProvider.IsChanged(String)](M_Tessa_Platform_Storage_IStorageObjectStateProvider_IsChanged.htm)  
##  __См. также
#### Ссылки
[CardRow - ](T_Tessa_Cards_CardRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
