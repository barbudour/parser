# CommandCollection.GetKeyForItem - метод
When implemented in a derived class, extracts the key from the specified
element.
##  __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override string GetKeyForItem(
    	Command item
    )
VB __Копировать
     Protected Overrides Function GetKeyForItem ( 
    	item As Command
    ) As String
C++ __Копировать
     protected:
    virtual String^ GetKeyForItem(
    	Command^ item
    ) override
F# __Копировать
     abstract GetKeyForItem : 
            item : Command -> string 
    override GetKeyForItem : 
            item : Command -> string 
#### Параметры
item [Command](T_Tessa_Platform_CommandLine_Command.htm)
    The element from which to extract the key.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
The key for the specified element.
##  __См. также
#### Ссылки
[CommandCollection - ](T_Tessa_Platform_CommandLine_CommandCollection.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
