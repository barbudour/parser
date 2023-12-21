# CardMetadataBinder - класс
Вспомогательный класс, осуществляющий действия с карточкой, требующие наличие
метаинформации.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardMetadataBinder : ICardMetadataBinder
VB __Копировать
     Public NotInheritable Class CardMetadataBinder
    	Implements ICardMetadataBinder
C++ __Копировать
     public ref class CardMetadataBinder sealed : ICardMetadataBinder
F# __Копировать
     [<SealedAttribute>]
    type CardMetadataBinder = 
        class
            interface ICardMetadataBinder
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardMetadataBinder
Implements
    [ICardMetadataBinder](T_Tessa_Cards_Metadata_ICardMetadataBinder.htm)
##  __Конструкторы
[CardMetadataBinder](M_Tessa_Cards_Metadata_CardMetadataBinder__ctor.htm)|
Создаёт экземпляр класса с указанием карточки и метаинформации, которая может
быть использована для карточки заданного типа.  
---|---  
## __Методы
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveRowAsync](M_Tessa_Cards_Metadata_CardMetadataBinder_RemoveRowAsync.htm)|
Выполняет удаление указанной строки из коллекционной или древовидной секции с
заданным именем, при этом учитывается возможное наличие строк в дочерних
секциях.  
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
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
