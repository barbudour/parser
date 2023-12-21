# CardTask.IsLockedExplicit - свойство
Признак того, что для задания требуется принудительно установить режим
просмотра [IsLocked](P_Tessa_Cards_CardTask_IsLocked.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool? IsLockedExplicit { get; set; }
VB __Копировать
     Public Property IsLockedExplicit As Boolean?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<bool> IsLockedExplicit {
    	Nullable<bool> get ();
    	void set (Nullable<bool> value);
    }
F# __Копировать
     member IsLockedExplicit : Nullable<bool> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
##  __Заметки
Это свойство не записывается в хранилище, поэтому оно эффективно только для
текущего декоратора.
## __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
