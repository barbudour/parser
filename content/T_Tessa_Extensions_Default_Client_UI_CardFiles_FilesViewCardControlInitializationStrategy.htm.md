# FilesViewCardControlInitializationStrategy - класс
Стратегия инициализации модели представления
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.UI.CardFiles](N_Tessa_Extensions_Default_Client_UI_CardFiles.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public class FilesViewCardControlInitializationStrategy : ViewCardControlInitializationStrategy
VB __Копировать
     Public Class FilesViewCardControlInitializationStrategy
    	Inherits ViewCardControlInitializationStrategy
C++ __Копировать
     public ref class FilesViewCardControlInitializationStrategy : public ViewCardControlInitializationStrategy
F# __Копировать
     type FilesViewCardControlInitializationStrategy = 
        class
            inherit ViewCardControlInitializationStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm) __ FilesViewCardControlInitializationStrategy
##  __Конструкторы
[FilesViewCardControlInitializationStrategy](M_Tessa_Extensions_Default_Client_UI_CardFiles_FilesViewCardControlInitializationStrategy__ctor.htm)|
Инициализирует новый экземпляр класса
FilesViewCardControlInitializationStrategy  
---|---  
##  __Свойства
[ContentItemsFactory](P_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_ContentItemsFactory.htm)|  
(Унаследован от
[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm))  
---|---  
[CreateMenuContextFunc](P_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_CreateMenuContextFunc.htm)|  
(Унаследован от
[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm))  
[ViewService](P_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_ViewService.htm)|  
(Унаследован от
[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm))  
##  __Методы
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
[InitializeContentAsync](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeContentAsync.htm)|
Вызывается для инициализации
[Content](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_Content.htm) и
т.п. в модели заданной в [!:context]  
(Унаследован от
[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm))  
[InitializeContextMenuAsync](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeContextMenuAsync.htm)|
Вызывается для инициализации
[ContextMenuGenerators](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_ContextMenuGenerators.htm)
в модели заданной в [!:context]  
(Унаследован от
[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm))  
[InitializeDataProviderAsync](M_Tessa_Extensions_Default_Client_UI_CardFiles_FilesViewCardControlInitializationStrategy_InitializeDataProviderAsync.htm)|  
(Переопределяет
[ViewCardControlInitializationStrategy.InitializeDataProviderAsync(CardViewControlInitializationContext)](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeDataProviderAsync.htm))  
[InitializeMetadataAsync](M_Tessa_Extensions_Default_Client_UI_CardFiles_FilesViewCardControlInitializationStrategy_InitializeMetadataAsync.htm)|  
(Переопределяет
[ViewCardControlInitializationStrategy.InitializeMetadataAsync(CardViewControlInitializationContext)](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeMetadataAsync.htm))  
[InitializePagingAsync](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializePagingAsync.htm)|
Вызывается для инициализации
[PagingMode](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_PagingMode.htm)
и т.п. в модели заданной в [!:context]  
(Унаследован от
[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm))  
[InitializeParametersAsync](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeParametersAsync.htm)|
Вызывается для инициализации
[Parameters](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_Parameters.htm)
в модели заданной в [!:context]  
(Унаследован от
[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm))  
[InitializeSortingAsync](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeSortingAsync.htm)|
Вызывается для инициализации [IViewSorting](T_Tessa_UI_Views_IViewSorting.htm)
в модели заданной в [!:context]  
(Унаследован от
[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm))  
[InitializeTableAsync](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeTableAsync.htm)|
Вызывается для инициализации
[Table](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_Table.htm) в модели
заданной в [!:context]  
(Унаследован от
[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ViewExistsAsync](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_ViewExistsAsync.htm)|
Проверяет, существует ли предсталвение с алиасом из контрола представления  
(Унаследован от
[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm))  
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
[Tessa.Extensions.Default.Client.UI.CardFiles - пространство
имён](N_Tessa_Extensions_Default_Client_UI_CardFiles.htm)
