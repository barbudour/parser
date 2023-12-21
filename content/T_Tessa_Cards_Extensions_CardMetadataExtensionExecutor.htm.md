# CardMetadataExtensionExecutor - класс
Объект, обеспечивающий выполнение расширений для метаинформации по типам
карточек
[ICardMetadataExtension](T_Tessa_Cards_Extensions_ICardMetadataExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardMetadataExtensionExecutor : ICardMetadataExtensionExecutor, 
    	IAsyncDisposable
VB __Копировать
     Public NotInheritable Class CardMetadataExtensionExecutor
    	Implements ICardMetadataExtensionExecutor, IAsyncDisposable
C++ __Копировать
     public ref class CardMetadataExtensionExecutor sealed : ICardMetadataExtensionExecutor, 
    	IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type CardMetadataExtensionExecutor = 
        class
            interface ICardMetadataExtensionExecutor
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardMetadataExtensionExecutor
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [ICardMetadataExtensionExecutor](T_Tessa_Cards_Extensions_ICardMetadataExtensionExecutor.htm)
##  __Конструкторы
[CardMetadataExtensionExecutor](M_Tessa_Cards_Extensions_CardMetadataExtensionExecutor__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[DisposeAsync](M_Tessa_Cards_Extensions_CardMetadataExtensionExecutor_DisposeAsync.htm)|
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
[ModifyMetadataAsync](M_Tessa_Cards_Extensions_CardMetadataExtensionExecutor_ModifyMetadataAsync.htm)|
Выполняет расширения, изменяющие метаинформацию по типам карточек после её
построения.  
[ModifyTypesAsync](M_Tessa_Cards_Extensions_CardMetadataExtensionExecutor_ModifyTypesAsync.htm)|
Выполняет расширения, изменяющие типы карточек, по которым затем будет
строиться метаинформация.  
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
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
