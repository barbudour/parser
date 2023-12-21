# BusinessProcessCardHelper.FillVirtualRow - метод
Метод для переноса данных их строки физической секции версии процесса в строку
виртуальной секции
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void FillVirtualRow(
    	CardRow versionRow,
    	CardRow virtualRow,
    	CardSection versionsSection = null
    )
VB __Копировать
     Public Shared Sub FillVirtualRow ( 
    	versionRow As CardRow,
    	virtualRow As CardRow,
    	Optional versionsSection As CardSection = Nothing
    )
C++ __Копировать
     public:
    static void FillVirtualRow(
    	CardRow^ versionRow, 
    	CardRow^ virtualRow, 
    	CardSection^ versionsSection = nullptr
    )
F# __Копировать
     static member FillVirtualRow : 
            versionRow : CardRow * 
            virtualRow : CardRow * 
            ?versionsSection : CardSection 
    (* Defaults:
            let _versionsSection = defaultArg versionsSection null
    *)
    -> unit 
#### Параметры
versionRow [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка физической секции версии процесса
virtualRow [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка виртуальной секции версии процесса
versionsSection [CardSection](T_Tessa_Cards_CardSection.htm) (Optional)
    Физическая секция с версиями процесса
##  __См. также
#### Ссылки
[BusinessProcessCardHelper -
](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
