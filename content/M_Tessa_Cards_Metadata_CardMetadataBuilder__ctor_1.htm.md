# CardMetadataBuilder(Func<ICardMetadataExtensionExecutor>) - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataBuilder(
    	Func<ICardMetadataExtensionExecutor> createExtensionExecutorFunc
    )
VB __Копировать
     Public Sub New ( 
    	createExtensionExecutorFunc As Func(Of ICardMetadataExtensionExecutor)
    )
C++ __Копировать
     public:
    CardMetadataBuilder(
    	Func<ICardMetadataExtensionExecutor^>^ createExtensionExecutorFunc
    )
F# __Копировать
     new : 
            createExtensionExecutorFunc : Func<ICardMetadataExtensionExecutor> -> CardMetadataBuilder
#### Параметры
createExtensionExecutorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardMetadataExtensionExecutor](T_Tessa_Cards_Extensions_ICardMetadataExtensionExecutor.htm)>
     Функция, создающая объект, выполняющий расширения для метаинформации по типам карточек. Функция не должна быть равна null и не должна возвращать null. 
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|  
---|---  
##  __См. также
#### Ссылки
[CardMetadataBuilder - ](T_Tessa_Cards_Metadata_CardMetadataBuilder.htm)
[CardMetadataBuilder -
перегрузка](Overload_Tessa_Cards_Metadata_CardMetadataBuilder__ctor.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
