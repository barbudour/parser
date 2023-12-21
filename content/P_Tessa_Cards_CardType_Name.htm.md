# CardType.Name - свойство
Отображаемое имя объекта.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public override string Name { get; set; }
VB __Копировать
    <NotNullAttribute>
    Public Overrides Property Name As String
    	Get
    	Set
C++ __Копировать
     public:
    [NotNullAttribute]
    virtual property String^ Name {
    	String^ get () override;
    	void set (String^ value) override;
    }
F# __Копировать
     [<NotNullAttribute>]
    abstract Name : string with get, set
    [<NotNullAttribute>]
    override Name : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
#### Реализации
[INamedEntry.Name](P_Tessa_Platform_INamedEntry_Name.htm)  
[INamedItem.Name](P_Tessa_Platform_Collections_INamedItem_Name.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardType - ](T_Tessa_Cards_CardType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
