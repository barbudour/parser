# CardTask.HistoryItemParentRowID - свойство
Ссылка на родительскую запись в истории заданий, которая учитывается только
при автоматическом создании записи в истории заданий в процессе сохранения
карточки. При создании и загрузке карточки поле не заполняется и равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? HistoryItemParentRowID { get; set; }
VB __Копировать
     Public Property HistoryItemParentRowID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<Guid> HistoryItemParentRowID {
    	Nullable<Guid> get ();
    	void set (Nullable<Guid> value);
    }
F# __Копировать
     member HistoryItemParentRowID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
