# CommandRouter - класс
Роутер команд, осуществляет поиск обработчиков команд и вызывает их исполнение
## __Definition
 **Пространство имён:**
[Tessa.Views.MessageServices](N_Tessa_Views_MessageServices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CommandRouter : ICommandRouter
VB __Копировать
     Public NotInheritable Class CommandRouter
    	Implements ICommandRouter
C++ __Копировать
     public ref class CommandRouter sealed : ICommandRouter
F# __Копировать
     [<SealedAttribute>]
    type CommandRouter = 
        class
            interface ICommandRouter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CommandRouter
Implements
    [ICommandRouter](T_Tessa_Views_MessageServices_ICommandRouter.htm)
##  __Конструкторы
[CommandRouter](M_Tessa_Views_MessageServices_CommandRouter__ctor.htm)|
Initializes a new instance of the CommandRouter class. Инициализирует новый
экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SubmitCommandAsync<TCommand>](M_Tessa_Views_MessageServices_CommandRouter_SubmitCommandAsync__1.htm)|
Осуществляет отправку команды command обработчику  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[ClearFilterAsync](M_Tessa_UI_Views_Workplaces_Tree_TreeItemExtender_ClearFilterAsync.htm)|
Сбрасывает параметры фильтра для списка параметров parameters  
(Определяется
[TreeItemExtender](T_Tessa_UI_Views_Workplaces_Tree_TreeItemExtender.htm))  
---|---  
[FilterAsync](M_Tessa_UI_Views_Workplaces_Tree_TreeItemExtender_FilterAsync.htm)|
Вызывает диалоговое окно фильтра для списка параметров parameters  
(Определяется
[TreeItemExtender](T_Tessa_UI_Views_Workplaces_Tree_TreeItemExtender.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Views.MessageServices - пространство
имён](N_Tessa_Views_MessageServices.htm)
