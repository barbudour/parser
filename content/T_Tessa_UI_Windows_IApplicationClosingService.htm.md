# IApplicationClosingService - интерфейс
Описание интерфейса реакции на закрытие главного окна приложения
## __Definition
 **Пространство имён:** [Tessa.UI.Windows](N_Tessa_UI_Windows.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationClosingService
VB __Копировать
     Public Interface IApplicationClosingService
C++ __Копировать
     public interface class IApplicationClosingService
F# __Копировать
     type IApplicationClosingService = interface end
##  __Методы
[RegisterClosingObserver](M_Tessa_UI_Windows_IApplicationClosingService_RegisterClosingObserver.htm)|
Регистрирует функцию observer вызываемую при попытке закрытия главного окна
приложения. Функция observer должна возвращать следующие возмные причины
отказа закрытия приложения если приложение может быть закрыто возвращает
nullc> если требуется подтверждение закрытия приложения от пользователя с
выдачей сообщения
[Message](P_Tessa_UI_Windows_CancelClosingReasonInfo_Message.htm) возвращает
[ClosingReason](P_Tessa_UI_Windows_CancelClosingReasonInfo_ClosingReason.htm)
установленный в [UserDefined](T_Tessa_UI_Windows_CancelClosingReason.htm) если
приложения не может быть закрыто в данный момент с выдачей сообщения
[Message](P_Tessa_UI_Windows_CancelClosingReasonInfo_Message.htm) возвращает
[ClosingReason](P_Tessa_UI_Windows_CancelClosingReasonInfo_ClosingReason.htm)
установленный в [CantClose](T_Tessa_UI_Windows_CancelClosingReason.htm)  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI.Windows - пространство имён](N_Tessa_UI_Windows.htm)
