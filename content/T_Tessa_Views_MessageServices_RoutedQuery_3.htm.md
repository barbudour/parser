# RoutedQuery<TQuery, TResult, TContext> \- класс
Базовый класс для создания перенаправляемых запросов
## __Definition
 **Пространство имён:**
[Tessa.Views.MessageServices](N_Tessa_Views_MessageServices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class RoutedQuery<TQuery, TResult, TContext> : IRoutedQuery<TResult>
    where TQuery : new(), RoutedQuery<TQuery, TResult, TContext>
VB __Копировать
     Public MustInherit Class RoutedQuery(Of TQuery As {New, RoutedQuery(Of TQuery, TResult, TContext)}, TResult, TContext)
    	Implements IRoutedQuery(Of TResult)
C++ __Копировать
    generic<typename TQuery, typename TResult, typename TContext>
    where TQuery : gcnew(), RoutedQuery<TQuery, TResult, TContext>
    public ref class RoutedQuery abstract : IRoutedQuery<TResult>
F# __Копировать
     [<AbstractClassAttribute>]
    type RoutedQuery<'TQuery, 'TResult, 'TContext when 'TQuery : new() and RoutedQuery<'TQuery, 'TResult, 'TContext>> = 
        class
            interface IRoutedQuery<'TResult>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RoutedQuery<TQuery, TResult, TContext>
Implements
    [IRoutedQuery](T_Tessa_Views_MessageServices_IRoutedQuery_1.htm)<TResult>
#### Параметры типа
TQuery
     Тип запроса 
TResult
     Тип результата выполнения запроса 
TContext
     Контекст запроса 
## __Конструкторы
[RoutedQuery<TQuery, TResult,
TContext>](M_Tessa_Views_MessageServices_RoutedQuery_3__ctor.htm)|
Initializes a new instance of the RoutedQuery<TQuery, TResult, TContext>
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Методы
[Create](M_Tessa_Views_MessageServices_RoutedQuery_3_Create.htm)|
Осуществляет создание запроса и инициализацию его контекстом context  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetContext](M_Tessa_Views_MessageServices_RoutedQuery_3_SetContext.htm)|
Вызывает установку контекста  
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
[Tessa.Views.MessageServices - пространство
имён](N_Tessa_Views_MessageServices.htm)
