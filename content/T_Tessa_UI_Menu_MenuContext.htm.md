# MenuContext - класс
Контекст, предоставляющий средства для генерации меню, например, посредством
интерфейса [IContextMenuProvider](T_Tessa_UI_Menu_IContextMenuProvider.htm).
## __Definition
 **Пространство имён:** [Tessa.UI.Menu](N_Tessa_UI_Menu.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class MenuContext : IMenuContext, 
    	IMenuActionGeneratorProvider, IUIContextExecutorProvider
VB __Копировать
     Public NotInheritable Class MenuContext
    	Implements IMenuContext, IMenuActionGeneratorProvider, IUIContextExecutorProvider
C++ __Копировать
     public ref class MenuContext sealed : IMenuContext, 
    	IMenuActionGeneratorProvider, IUIContextExecutorProvider
F# __Копировать
     [<SealedAttribute>]
    type MenuContext = 
        class
            interface IMenuContext
            interface IMenuActionGeneratorProvider
            interface IUIContextExecutorProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ MenuContext
Implements
    [IUIContextExecutorProvider](T_Tessa_UI_IUIContextExecutorProvider.htm), [IMenuActionGeneratorProvider](T_Tessa_UI_Menu_IMenuActionGeneratorProvider.htm), [IMenuContext](T_Tessa_UI_Menu_IMenuContext.htm)
##  __Конструкторы
[MenuContext](M_Tessa_UI_Menu_MenuContext__ctor.htm)|  Создаёт экземпляр
класса с указанием его зависимостей.  
---|---  
## __Свойства
[Icons](P_Tessa_UI_Menu_MenuContext_Icons.htm)|  Возвращает контекстное меню,
доступное для текущей модели представления. Если возвращается null, пустая
коллекция или коллекция из скрытых элементов, то меню при этом не
отображается.  
---|---  
[MenuActionGenerator](P_Tessa_UI_Menu_MenuContext_MenuActionGenerator.htm)|
Используемый объект [Tessa.UI.Menu.IMenuActionGenerator].  
[UIContextExecutorAsync](P_Tessa_UI_Menu_MenuContext_UIContextExecutorAsync.htm)|
Делегат, выполняющий заданное действие в контексте [Tessa.UI.IUIContext].  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
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
[Tessa.UI.Menu - пространство имён](N_Tessa_UI_Menu.htm)
