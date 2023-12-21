# CardFile.CategoryID - свойство
Идентификатор категории файла или null, если категория файла не указана или
выбранная категория не имеет идентификатора. Значение
[CategoryCaption](P_Tessa_Cards_CardFile_CategoryCaption.htm) обязательно
должно быть указано для того, чтобы файл был включён в категорию, а значение
CategoryID является опциональным для идентификации категории.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? CategoryID { get; set; }
VB __Копировать
     Public Property CategoryID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<Guid> CategoryID {
    	Nullable<Guid> get ();
    	void set (Nullable<Guid> value);
    }
F# __Копировать
     member CategoryID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
