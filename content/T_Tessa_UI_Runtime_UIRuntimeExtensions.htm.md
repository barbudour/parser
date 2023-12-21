# UIRuntimeExtensions - класс
Методы-расширения для пространства имён Tessa.UI.Runtime.
## __Definition
 **Пространство имён:** [Tessa.UI.Runtime](N_Tessa_UI_Runtime.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class UIRuntimeExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class UIRuntimeExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class UIRuntimeExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type UIRuntimeExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UIRuntimeExtensions
##  __Методы
[AddResourcesTo](M_Tessa_UI_Runtime_UIRuntimeExtensions_AddResourcesTo.htm)|
Добавляет зарегистрированные словари ресурсов в заданное приложение. Если
приложение содержит некоторые словари ресурсов с таким же местоположением, то
метод не добавляет словари повторно.  
---|---  
[RegisterSessionsUI](M_Tessa_UI_Runtime_UIRuntimeExtensions_RegisterSessionsUI.htm)|
Выполняет регистрацию всех основных API, требуемых на клиенте с учётом UI, в
заданном контейнере Unity. При использовании данного метода рекомендуется не
вызывать метод RegisterSessionsOnClient.  
## __См. также
#### Ссылки
[Tessa.UI.Runtime - пространство имён](N_Tessa_UI_Runtime.htm)
