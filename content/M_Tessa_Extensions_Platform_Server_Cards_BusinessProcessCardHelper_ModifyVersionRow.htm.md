# BusinessProcessCardHelper.ModifyVersionRow - метод
Метод для заполнения полей строки версии процесса, которые должны заполняться
при изменении процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void ModifyVersionRow(
    	ISession session,
    	CardRow row
    )
VB __Копировать
     Public Shared Sub ModifyVersionRow ( 
    	session As ISession,
    	row As CardRow
    )
C++ __Копировать
     public:
    static void ModifyVersionRow(
    	ISession^ session, 
    	CardRow^ row
    )
F# __Копировать
     static member ModifyVersionRow : 
            session : ISession * 
            row : CardRow -> unit 
#### Параметры
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Текущая сессия.
row [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка версии процесса.
##  __См. также
#### Ссылки
[BusinessProcessCardHelper -
](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
