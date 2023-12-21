# CardRequestTypes.ResetUserSettings - поле
Запрос на сброс всех личных настроек пользователя. В параметре
[CardID](P_Tessa_Cards_CardRequest_CardID.htm) содержится идентификатор
сотрудника, для которого выполняется сброс. Обработчик по умолчанию
выполняется только для текущего пользователя или, если пользователь является
администратором, то для любого пользователя.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static readonly Guid ResetUserSettings
VB __Копировать
     Public Shared ReadOnly ResetUserSettings As Guid
C++ __Копировать
     public:
    static initonly Guid ResetUserSettings
F# __Копировать
     static val ResetUserSettings: Guid
#### Значение поля
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)
##  __См. также
#### Ссылки
[CardRequestTypes - ](T_Tessa_Cards_CardRequestTypes.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
