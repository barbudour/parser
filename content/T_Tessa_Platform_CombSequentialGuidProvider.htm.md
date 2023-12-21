# CombSequentialGuidProvider - класс
Объект, выполняющий создание уникальный идентификаторов таким образом, чтобы
каждый следующий созданный идентификатор был последовательным, в соответствии
с правилами переданного объекта
[IGuidCombProvider](T_Tessa_Platform_GuidComb_IGuidCombProvider.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CombSequentialGuidProvider : ISequentialGuidProvider
VB __Копировать
     Public NotInheritable Class CombSequentialGuidProvider
    	Implements ISequentialGuidProvider
C++ __Копировать
     public ref class CombSequentialGuidProvider sealed : ISequentialGuidProvider
F# __Копировать
     [<SealedAttribute>]
    type CombSequentialGuidProvider = 
        class
            interface ISequentialGuidProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CombSequentialGuidProvider
Implements
    [ISequentialGuidProvider](T_Tessa_Platform_ISequentialGuidProvider.htm)
##  __Конструкторы
[CombSequentialGuidProvider](M_Tessa_Platform_CombSequentialGuidProvider__ctor.htm)|
Создаёт экземпляр объекта с указанием его зависимостей.  
---|---  
## __Методы
[CreateAsync](M_Tessa_Platform_CombSequentialGuidProvider_CreateAsync.htm)|
Создаёт и возвращает уникальный идентификатор.  
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
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
