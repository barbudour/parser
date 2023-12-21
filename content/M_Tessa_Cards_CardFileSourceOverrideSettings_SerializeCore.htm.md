# CardFileSourceOverrideSettings.SerializeCore - метод
Выполняет сериализацию полей объекта в заданное хранилище.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override void SerializeCore(
    	Dictionary<string, Object> storage
    )
VB __Копировать
     Protected Overrides Sub SerializeCore ( 
    	storage As Dictionary(Of String, Object)
    )
C++ __Копировать
     protected:
    virtual void SerializeCore(
    	Dictionary<String^, Object^>^ storage
    ) override
F# __Копировать
     abstract SerializeCore : 
            storage : Dictionary<string, Object> -> unit 
    override SerializeCore : 
            storage : Dictionary<string, Object> -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, в которое сериализуется объект.
##  __См. также
#### Ссылки
[CardFileSourceOverrideSettings -
](T_Tessa_Cards_CardFileSourceOverrideSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
