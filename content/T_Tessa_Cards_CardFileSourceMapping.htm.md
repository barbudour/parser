# CardFileSourceMapping - класс
Отображение между источниками контента для файлов одной и той же карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardFileSourceMapping : ICardFileSourceMapping, 
    	ISealable
VB __Копировать
     Public NotInheritable Class CardFileSourceMapping
    	Implements ICardFileSourceMapping, ISealable
C++ __Копировать
     public ref class CardFileSourceMapping sealed : ICardFileSourceMapping, 
    	ISealable
F# __Копировать
     [<SealedAttribute>]
    type CardFileSourceMapping = 
        class
            interface ICardFileSourceMapping
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardFileSourceMapping
Implements
    [ICardFileSourceMapping](T_Tessa_Cards_ICardFileSourceMapping.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[CardFileSourceMapping](M_Tessa_Cards_CardFileSourceMapping__ctor.htm)|
Инициализирует новый экземпляр класса CardFileSourceMapping  
---|---  
##  __Свойства
[IsSealed](P_Tessa_Cards_CardFileSourceMapping_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
---|---  
##  __Методы
[CreateContentSource](M_Tessa_Cards_CardFileSourceMapping_CreateContentSource.htm)|
Создаёт источник контента файла, который можно использовать в отображении без
потерь в производительности.  
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
[Map](M_Tessa_Cards_CardFileSourceMapping_Map.htm)|  Создаёт отображение между
файлом с заданными параметрами отображения и указанным объектом источника
контента файла.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Seal](M_Tessa_Cards_CardFileSourceMapping_Seal.htm)| Защищает объект от
изменений.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGet](M_Tessa_Cards_CardFileSourceMapping_TryGet.htm)|  Возвращает источник
контента файла для заданных параметров отображения или null, если отображение
не найдено.  
## __Методы расширения
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
