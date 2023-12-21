# LimitedPoolExpirationTokenSource - класс
Объект, по которому токены определяют признак того, что время жизни объектов в
пуле истекло. В момент вызова
[Dispose()](M_Tessa_Platform_Collections_LimitedPoolExpirationTokenSource_Dispose.htm)
все токены
[Token](P_Tessa_Platform_Collections_LimitedPoolExpirationTokenSource_Token.htm)
будут считаться истёкшими по времени жизни.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class LimitedPoolExpirationTokenSource : IDisposable
VB __Копировать
     Public NotInheritable Class LimitedPoolExpirationTokenSource
    	Implements IDisposable
C++ __Копировать
     public ref class LimitedPoolExpirationTokenSource sealed : IDisposable
F# __Копировать
     [<SealedAttribute>]
    type LimitedPoolExpirationTokenSource = 
        class
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LimitedPoolExpirationTokenSource
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Конструкторы
[LimitedPoolExpirationTokenSource](M_Tessa_Platform_Collections_LimitedPoolExpirationTokenSource__ctor.htm)|
Инициализирует новый экземпляр класса LimitedPoolExpirationTokenSource  
---|---  
##  __Свойства
[IsExpired](P_Tessa_Platform_Collections_LimitedPoolExpirationTokenSource_IsExpired.htm)|
Признак того, что срок действия связанных объектов установлен как истёкший.  
---|---  
[Token](P_Tessa_Platform_Collections_LimitedPoolExpirationTokenSource_Token.htm)|
Токен, который определяет признак того, что время жизни объекта в пуле
истекло.  
## __Методы
[Dispose](M_Tessa_Platform_Collections_LimitedPoolExpirationTokenSource_Dispose.htm)|
Освобождает ресурсы, занимаемые объектом.  
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
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
