# CardType.ID - свойство
Идентификатор объекта.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [PrimaryKeyAttribute]
    [IdentityAttribute]
    [NotNullAttribute]
    [ColumnAttribute(SkipOnUpdate = true)]
    public Guid ID { get; set; }
VB __Копировать
    <PrimaryKeyAttribute>
    <IdentityAttribute>
    <NotNullAttribute>
    <ColumnAttribute(SkipOnUpdate := true)>
    Public Property ID As Guid
    	Get
    	Set
C++ __Копировать
     public:
    [PrimaryKeyAttribute]
    [IdentityAttribute]
    [NotNullAttribute]
    [ColumnAttribute(SkipOnUpdate = true)]
    virtual property Guid ID {
    	Guid get () sealed;
    	void set (Guid value) sealed;
    }
F# __Копировать
     [<PrimaryKeyAttribute>]
    [<IdentityAttribute>]
    [<NotNullAttribute>]
    [<ColumnAttribute(SkipOnUpdate = true)>]
    abstract ID : Guid with get, set
    [<PrimaryKeyAttribute>]
    [<IdentityAttribute>]
    [<NotNullAttribute>]
    [<ColumnAttribute(SkipOnUpdate = true)>]
    override ID : Guid with get, set
#### Значение свойства
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)
#### Реализации
[INamedEntry.ID](P_Tessa_Platform_INamedEntry_ID.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardType - ](T_Tessa_Cards_CardType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
