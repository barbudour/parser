# CardFileSourceOverride.IsDatabase - свойство
Признак того, что местоположение соответствует базе данных, а не файловой
папке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool? IsDatabase { get; set; }
VB __Копировать
     Public Property IsDatabase As Boolean?
    	Get
    	Set
C++ __Копировать
     public:
    virtual property Nullable<bool> IsDatabase {
    	Nullable<bool> get () sealed;
    	void set (Nullable<bool> value) sealed;
    }
F# __Копировать
     abstract IsDatabase : Nullable<bool> with get, set
    override IsDatabase : Nullable<bool> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
#### Реализации
[ICardFileSourceOverride.IsDatabase](P_Tessa_Cards_ICardFileSourceOverride_IsDatabase.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardFileSourceOverride - ](T_Tessa_Cards_CardFileSourceOverride.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
