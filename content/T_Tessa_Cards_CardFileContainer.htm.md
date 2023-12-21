# CardFileContainer - класс
Контейнер, содержащий информацию по карточке и её файлам.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardFileContainer : ICardFileContainer, 
    	IAsyncDisposable
VB __Копировать
     Public NotInheritable Class CardFileContainer
    	Implements ICardFileContainer, IAsyncDisposable
C++ __Копировать
     public ref class CardFileContainer sealed : ICardFileContainer, 
    	IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type CardFileContainer = 
        class
            interface ICardFileContainer
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardFileContainer
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm)
##  __Конструкторы
[CardFileContainer](M_Tessa_Cards_CardFileContainer__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Card](P_Tessa_Cards_CardFileContainer_Card.htm)| Карточка.  
---|---  
[CreationResult](P_Tessa_Cards_CardFileContainer_CreationResult.htm)|
Результат создания текущего объекта. Может содержать ошибки, связанные с
получением файлов.  
[FileContainer](P_Tessa_Cards_CardFileContainer_FileContainer.htm)| Файлы,
относящиеся к карточке.  
[Manager](P_Tessa_Cards_CardFileContainer_Manager.htm)| Объект, который создал
текущий контейнер.  
##  __Методы
[DisposeAsync](M_Tessa_Cards_CardFileContainer_DisposeAsync.htm)| Освобождает
ресурсы, занимаемые объектом.  
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
[StoreAsync](M_Tessa_Cards_CardExtensions_StoreAsync.htm)|  Сохраняет карточку
из текущего контейнера и контент её файлов, при этом позволяет асинхронно
отслеживать её состояние. В процессе сохранения карточка в контейнере и её
файлы не изменяются, поэтому метод безопасно вызывать повторно.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
