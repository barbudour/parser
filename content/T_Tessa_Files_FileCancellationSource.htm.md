# FileCancellationSource - класс
Объект, управляющий отменой асинхронных операций с файлами.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileCancellationSource : IFileCancellationSource, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class FileCancellationSource
    	Implements IFileCancellationSource, IDisposable
C++ __Копировать
     public ref class FileCancellationSource sealed : IFileCancellationSource, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type FileCancellationSource = 
        class
            interface IFileCancellationSource
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileCancellationSource
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IFileCancellationSource](T_Tessa_Files_IFileCancellationSource.htm)
##  __Конструкторы
[FileCancellationSource](M_Tessa_Files_FileCancellationSource__ctor.htm)|
Создаёт экземпляр класса с указанием функции, создающей объект
[CancellationTokenSource](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtokensource).  
---|---  
## __Свойства
[IsCancellationRequested](P_Tessa_Files_FileCancellationSource_IsCancellationRequested.htm)|
Признак того, что текущий объект запросил отмену связанных с ним асинхронных
операций.  
---|---  
[Token](P_Tessa_Files_FileCancellationSource_Token.htm)| Токен, используемый в
асинхронных операциях, которые могут быть отменены.  
##  __Методы
[Cancel](M_Tessa_Files_FileCancellationSource_Cancel.htm)| Отменяет все
асинхронные операции, связанные с текущим объектом.  
---|---  
[Dispose](M_Tessa_Files_FileCancellationSource_Dispose.htm)| Освобождает
ресурсы, занимаемые объектом.  
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
[Reset](M_Tessa_Files_FileCancellationSource_Reset.htm)|  Восстанавливает
возможность выполнения для асинхронных операций, которые будут связаны с
текущим объектом. Если отмена ещё не выполнялась или ни одной связанной
асинхронной операции не создано, то метод не выполняет действий.  
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
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
