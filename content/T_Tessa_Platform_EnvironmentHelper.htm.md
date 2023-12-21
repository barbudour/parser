# EnvironmentHelper - класс
Класс, содержащий вспомогательную информацию о системе.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class EnvironmentHelper
VB __Копировать
     Public NotInheritable Class EnvironmentHelper
C++ __Копировать
     public ref class EnvironmentHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type EnvironmentHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ EnvironmentHelper
##  __Свойства
[NetRuntimeFriendlyName](P_Tessa_Platform_EnvironmentHelper_NetRuntimeFriendlyName.htm)|
Название исполняющей среды .NET для отображения пользователю с указанием её
версии. Возвращается пустая строка, если не удалось определить название.  
---|---  
[OSFriendlyName](P_Tessa_Platform_EnvironmentHelper_OSFriendlyName.htm)|
Название операционной системы для отображения пользователю или пустая строка,
если не удалось определить название.  
[OSQualifiedFriendlyName](P_Tessa_Platform_EnvironmentHelper_OSQualifiedFriendlyName.htm)|
Название операционной системы с указанием разрядности и сервис-пака для
отображения пользователю или пустая строка, если не удалось определить
название.  
[WindowsTerminalSessionID](P_Tessa_Platform_EnvironmentHelper_WindowsTerminalSessionID.htm)|
Идентификатор терминальной сессии, в рамках которой работает текущий процесс.
Свойство доступно только для Windows.  
## __Методы
[TryGetWindowsVersion](M_Tessa_Platform_EnvironmentHelper_TryGetWindowsVersion.htm)|
Возвращает текущую версию Windows по информации в имени ОС
[OSFriendlyName](P_Tessa_Platform_EnvironmentHelper_OSFriendlyName.htm) или
null, если версию не удалось определить. Метод доступен только для Windows.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
