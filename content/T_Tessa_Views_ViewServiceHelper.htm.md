# ViewServiceHelper - класс
Методы расширения для [IViewService](T_Tessa_Views_IViewService.htm)
##  __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ViewServiceHelper
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class ViewServiceHelper
C++ __Копировать
    [ExtensionAttribute]
    public ref class ViewServiceHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type ViewServiceHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ViewServiceHelper
##  __Методы
[TryGetViewAsync](M_Tessa_Views_ViewServiceHelper_TryGetViewAsync.htm)|
Осуществляет попытку получения представления по метаданным объекта дерева
рабочего места. В случае если представление доступно будет возвращена ссылка
на представление. Если доступ к представлению для текущего пользователя
запрещен или объект не найден будет возвращен null  
---|---  
## __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
