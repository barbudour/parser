# IMessageProvider - интерфейс
Объект, обеспечивающий вывод сообщений. Сообщения могут выводиться как в виде
диалоговых окон для пользователя, так и в лог. Используется, например, для
вывода сообщений в [IApplication](T_Tessa_Platform_Runtime_IApplication.htm).
Зарегистрирован на клиенте и на сервере.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMessageProvider
VB __Копировать
     Public Interface IMessageProvider
C++ __Копировать
     public interface class IMessageProvider
F# __Копировать
     type IMessageProvider = interface end
##  __Методы
[ConfirmAsync](M_Tessa_Platform_Runtime_IMessageProvider_ConfirmAsync.htm)|
Выводит заданное сообщение и ожидает ответа да/нет. Возвращает признак того,
что пользователь выбрал "да".  
---|---  
[ShowExceptionAsync](M_Tessa_Platform_Runtime_IMessageProvider_ShowExceptionAsync.htm)|
Выводит информацию по исключению.  
[ShowNotEmptyAsync](M_Tessa_Platform_Runtime_IMessageProvider_ShowNotEmptyAsync.htm)|
Выводит сообщение с результатом валидации, если он не пустой.  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
