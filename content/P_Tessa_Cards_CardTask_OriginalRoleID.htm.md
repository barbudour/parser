# CardTask.OriginalRoleID - свойство
Идентификатор текущей роли [RoleID](P_Tessa_Cards_CardTask_RoleID.htm), если
роль изменяется с флагом [UpdateRole](T_Tessa_Cards_CardTaskFlags.htm), или
null, если роль не изменяется или если значение ещё не заполнено платформой.
Это свойство используется платформой, не рекомендуется устанавливать его
значение вручную.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? OriginalRoleID { get; set; }
VB __Копировать
     Public Property OriginalRoleID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<Guid> OriginalRoleID {
    	Nullable<Guid> get ();
    	void set (Nullable<Guid> value);
    }
F# __Копировать
     member OriginalRoleID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Заметки
Это свойство не записывается в хранилище, поэтому оно эффективно только для
текущего декоратора.
## __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
