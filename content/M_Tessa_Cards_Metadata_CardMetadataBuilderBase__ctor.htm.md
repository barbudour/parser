# CardMetadataBuilderBase - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected CardMetadataBuilderBase(
    	Func<ICardMetadataExtensionExecutor> createExtensionExecutorFunc
    )
VB __Копировать
     Protected Sub New ( 
    	createExtensionExecutorFunc As Func(Of ICardMetadataExtensionExecutor)
    )
C++ __Копировать
     protected:
    CardMetadataBuilderBase(
    	Func<ICardMetadataExtensionExecutor^>^ createExtensionExecutorFunc
    )
F# __Копировать
     new : 
            createExtensionExecutorFunc : Func<ICardMetadataExtensionExecutor> -> CardMetadataBuilderBase
#### Параметры
createExtensionExecutorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardMetadataExtensionExecutor](T_Tessa_Cards_Extensions_ICardMetadataExtensionExecutor.htm)>
     Функция, создающая объект, выполняющий расширения для метаинформации по типам карточек. Функция не должна быть равна null и не должна возвращать null. 
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|  
---|---  
##  __См. также
#### Ссылки
[CardMetadataBuilderBase -
](T_Tessa_Cards_Metadata_CardMetadataBuilderBase.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
