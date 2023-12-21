# CardTableViewInitializationStrategy - класс
стратегия инициализации таблицы в представлении
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class CardTableViewInitializationStrategy : ViewCardControlInitializationStrategy
VB __Копировать
     Public Class CardTableViewInitializationStrategy
    	Inherits ViewCardControlInitializationStrategy
C++ __Копировать
     public ref class CardTableViewInitializationStrategy : public ViewCardControlInitializationStrategy
F# __Копировать
     type CardTableViewInitializationStrategy = 
        class
            inherit ViewCardControlInitializationStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm) __ CardTableViewInitializationStrategy
##  __Конструкторы
[CardTableViewInitializationStrategy](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewInitializationStrategy__ctor.htm)|
Инициализирует новый экземпляр класса CardTableViewInitializationStrategy  
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
[InitializeContentAsync](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewInitializationStrategy_InitializeContentAsync.htm)|
Убираем ненужные кнопки и копируем кнопки дял пейджинга из верхней панели в
нижнюю.  
(Переопределяет
[ViewCardControlInitializationStrategy.InitializeContentAsync(CardViewControlInitializationContext)](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeContentAsync.htm))  
[InitializeContextMenuAsync](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeContextMenuAsync.htm)|
Вызывается для инициализации
[ContextMenuGenerators](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_ContextMenuGenerators.htm)
в модели заданной в [!:context]  
(Унаследован от
[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm))  
[InitializeDataProviderAsync](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewInitializationStrategy_InitializeDataProviderAsync.htm)|
Провайдер данные не используется  
(Переопределяет
[ViewCardControlInitializationStrategy.InitializeDataProviderAsync(CardViewControlInitializationContext)](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeDataProviderAsync.htm))  
[InitializeMetadataAsync](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewInitializationStrategy_InitializeMetadataAsync.htm)|
Инициализируем метаданные значениями, которые задали в конструкторе контрола
из настроек контрола.  
(Переопределяет
[ViewCardControlInitializationStrategy.InitializeMetadataAsync(CardViewControlInitializationContext)](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeMetadataAsync.htm))  
[InitializePagingAsync](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewInitializationStrategy_InitializePagingAsync.htm)|  
(Переопределяет
[ViewCardControlInitializationStrategy.InitializePagingAsync(CardViewControlInitializationContext)](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializePagingAsync.htm))  
[InitializeParametersAsync](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeParametersAsync.htm)|
Вызывается для инициализации
[Parameters](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_Parameters.htm)
в модели заданной в [!:context]  
(Унаследован от
[ViewCardControlInitializationStrategy](T_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy.htm))  
[InitializeSortingAsync](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewInitializationStrategy_InitializeSortingAsync.htm)|  
(Переопределяет
[ViewCardControlInitializationStrategy.InitializeSortingAsync(CardViewControlInitializationContext)](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeSortingAsync.htm))  
[InitializeTableAsync](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewInitializationStrategy_InitializeTableAsync.htm)|  
(Переопределяет
[ViewCardControlInitializationStrategy.InitializeTableAsync(CardViewControlInitializationContext)](M_Tessa_UI_Cards_Controls_ViewCardControlInitializationStrategy_InitializeTableAsync.htm))  
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
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
