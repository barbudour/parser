# TreeViewItemTestExtension - класс
Тестовое расширение для узлов дерева рабочего места. Добавляет в контекстное
меню узла дерева РМ новый элемент.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Views](N_Tessa_Extensions_Default_Client_Views.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class TreeViewItemTestExtension : ITreeItemExtension, 
    	IWorkplaceExtension<ITreeItem>
VB __Копировать
     Public NotInheritable Class TreeViewItemTestExtension
    	Implements ITreeItemExtension, IWorkplaceExtension(Of ITreeItem)
C++ __Копировать
     public ref class TreeViewItemTestExtension sealed : ITreeItemExtension, 
    	IWorkplaceExtension<ITreeItem^>
F# __Копировать
     [<SealedAttribute>]
    type TreeViewItemTestExtension = 
        class
            interface ITreeItemExtension
            interface IWorkplaceExtension<ITreeItem>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TreeViewItemTestExtension
Implements
    [IWorkplaceExtension](T_Tessa_UI_Views_Extensions_IWorkplaceExtension_1.htm)<[ITreeItem](T_Tessa_UI_Views_Workplaces_Tree_ITreeItem.htm)>, [ITreeItemExtension](T_Tessa_UI_Views_ITreeItemExtension.htm)
##  __Заметки
У расширения есть конфигуратор
[TreeViewItemTestExtensionConfigurator](T_Tessa_Extensions_Default_Client_Views_TreeViewItemTestExtensionConfigurator.htm).
## __Конструкторы
[TreeViewItemTestExtension](M_Tessa_Extensions_Default_Client_Views_TreeViewItemTestExtension__ctor.htm)|
Инициализирует новый экземпляр класса TreeViewItemTestExtension  
---|---  
##  __Методы
[Clone](M_Tessa_Extensions_Default_Client_Views_TreeViewItemTestExtension_Clone.htm)|
Вызывается при клонировании модели source в контексте context  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Initialize](M_Tessa_Extensions_Default_Client_Views_TreeViewItemTestExtension_Initialize.htm)|
Вызывается после создания модели model для инициализации в UI  
[Initialized](M_Tessa_Extensions_Default_Client_Views_TreeViewItemTestExtension_Initialized.htm)|
Вызывается после создания модели model перед отображении в UI  
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
[Tessa.Extensions.Default.Client.Views - пространство
имён](N_Tessa_Extensions_Default_Client_Views.htm)
